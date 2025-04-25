import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import { getAuth, signInWithPopup, GithubAuthProvider, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";

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
const auth = getAuth(app);
const provider = new GithubAuthProvider();

document.getElementById('github-btn').addEventListener('click', () => {
  signInWithPopup(auth, provider)
    .then((result) => {
      const user = result.user;
      console.log("User Info:", user);

     
      window.location.href = "http://127.0.0.1:5000/dashboard";
    })
    .catch((error) => {
      console.error("Error during GitHub login:", error);
    });
});


onAuthStateChanged(auth, (user) => {
  if (user) {
    if (window.location.pathname !== '/dashboard') {
      window.location.href = "http://127.0.0.1:5000/dashboard"; 
    }
  }
});
