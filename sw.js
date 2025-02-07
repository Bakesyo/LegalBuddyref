const CACHE_NAME = 'lawsuit-buddy-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/favicon.ico',
  '/images/hero-bg.webp',
  '/images/hero-bg-mobile.webp'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
