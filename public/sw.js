const CACHE_NAME = 'legal-buddy-v1';
const URLS_TO_CACHE = [
  '/',
  '/index.html',
  '/success.html',
  '/404.html',
  '/styles/main.css',
  '/images/logo.png',
  '/favicon.ico',
  '/offline.html'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(URLS_TO_CACHE))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
      .catch(() => {
        // Return the offline page if both the cache and network are unavailable
        return caches.match('/offline.html');
      })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
    })
  );
});
