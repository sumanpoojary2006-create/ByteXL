// Vercel serves only these static files. All authenticated uploads and product
// updates go to the separately hosted API below.
window.IMAGE_CONVERTER_CONFIG = Object.freeze({
  apiBase: "https://bytexl-image-converter-api.onrender.com"
});
