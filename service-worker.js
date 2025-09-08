// service-worker.js
self.addEventListener("install", (event) => {
  console.log("✅ Service Worker instalado.");
});

self.addEventListener("activate", (event) => {
  console.log("🚀 Service Worker ativado.");
});

self.addEventListener("fetch", (event) => {
  // Neste exemplo não cacheamos nada,
  // só deixamos o request seguir normalmente
  console.log("🔎 Requisição interceptada:", event.request.url);
});
