import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-analytics.js";

  const firebaseConfig = {
    apiKey: "AIzaSyBnrOLlosTDGHCxXKZdFrO_ev-Oy2Ruv3U",
    authDomain: "nexora-213e2.firebaseapp.com",
    projectId: "nexora-213e2",
    storageBucket: "nexora-213e2.firebasestorage.app",
    messagingSenderId: "998457123271",
    appId: "1:998457123271:web:a26d2806f52c35479b39e2",
    measurementId: "G-8YMEDHQCEL"
  };

  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
