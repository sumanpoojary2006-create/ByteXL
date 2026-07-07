const http = require("http");
const handler = require("./app");
const port = Number(process.env.PORT || 8770);

const server = http.createServer(handler);

server.listen(port, () => {
  console.log(`Coding question uploader running at http://127.0.0.1:${port}`);
});
