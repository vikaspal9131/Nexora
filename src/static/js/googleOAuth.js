import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-analytics.js";
import {getAuth,signInWithPopup,GoogleAuthProvider,signOut} from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";

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
const analytics = getAnalytics(app);
const auth = getAuth();
const provider = new GoogleAuthProvider();


document.getElementById("google-btn").addEventListener("click", () => {
  signInWithPopup(auth, provider)
    .then((result) => {
      const user = result.user;
      alert("Welcome " + user.displayName);
      window.location.href = "/dashboard"; 
    })
    .catch((error) => {
      console.error("Login error:", error);
      alert("Login failed! Check console.");
    });
});



