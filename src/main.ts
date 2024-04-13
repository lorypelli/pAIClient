import App from "./App.svelte";
import './style.css';
let app = {};
const e = document.getElementById("app");
if (e) {
  app = new App({
    target: e,
  });
}

export default app;
