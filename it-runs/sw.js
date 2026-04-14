// IT RUNS — service worker
// Bump CACHE on every deploy you want users to hard-refresh to.
const CACHE = 'it-runs-v3';
const SCOPE_URL = new URL('./', self.location).pathname; // '/co-creation/it-runs/'
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './it-runs-dashboard-green.jsx',
  './icon.svg',
  './icon-192.png',
  './icon-512.png',
  './icon-512-maskable.png'
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

// Strategy:
//   - navigate requests  -> network-first, fall back to cached index.html
//     (mirrors MoonYou's workbox NavigationRoute behaviour)
//   - .jsx                -> network-first, fall back to cache (fast iteration)
//   - everything else     -> cache-first, fall back to network
self.addEventListener('fetch', (e) => {
  const req = e.request;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // Navigation fallback — any HTML page load within scope serves index.html offline.
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

  if (url.pathname.endsWith('.jsx')) {
    e.respondWith(
      fetch(req)
        .then((r) => {
          const copy = r.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
          return r;
        })
        .catch(() => caches.match(req))
    );
    return;
  }

  e.respondWith(
    caches.match(req).then((r) => r || fetch(req))
  );
});
