import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyAjjavWClMuq1urBMFBsp45cfVjp3cJ_3g",
  authDomain: "nexora-87f6a.firebaseapp.com",
  projectId: "nexora-87f6a",
  storageBucket: "nexora-87f6a.firebasestorage.app",
  messagingSenderId: "773823504351",
  appId: "1:773823504351:web:15b0943c5e35fd1be5ae6a",
  measurementId: "G-RCPQ51MY2G"
};  

const app = initializeApp(firebaseConfig);
const auth = getAuth();  

document.addEventListener("DOMContentLoaded", () => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        const photoURL = user.photoURL;
        console.log("User photo URL:", photoURL);
        if (photoURL) {
          document.getElementById("userPhoto").src = photoURL;
        }
        document.body.style.display = "block";
      } else {
        window.location.href = "/login";
      }
    });
});