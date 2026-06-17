// IT RUNS (template) — service worker
// Bump CACHE whenever you want installed users to pick up a new index.html.
const CACHE = 'it-runs-template-v1';
const SCOPE_URL = new URL('./', self.location).pathname;
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(ASSETS).catch(() => {}))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// navigate -> network-first, fall back to cached index.html (offline)
// same-origin assets -> cache-first
// (React/Babel come from a CDN and are cached by the browser's HTTP cache)
self.addEventListener('fetch', (e) => {
  const req = e.request;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req)
        .then((r) => {
          const copy = r.clone();
          caches.open(CACHE).then((c) => c.put(SCOPE_URL + 'index.html', copy));
          return r;
        })
        .catch(() =>
          caches.match(SCOPE_URL + 'index.html').then((r) => r || caches.match('./'))
        )
    );
    return;
  }

  e.respondWith(
    caches.match(req).then((r) => r || fetch(req))
  );
});
