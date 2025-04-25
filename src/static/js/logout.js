import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import {getAuth , signOut} from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";

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


document.getElementById("logout-btn").addEventListener("click", () => {
  document.getElementById("logout-modal").style.display = "flex";
});

const confirmLogout = document.getElementById("confirm-logout");
const cancelLogout = document.getElementById("cancel-logout");
const logoutModal = document.getElementById("logout-modal");

confirmLogout.addEventListener("click", () => {
  signOut(auth)
    .then(() => {
      window.location.href = "/"; 
    })
    .catch((error) => {
      console.error("Logout failed with error code:", error.code);
      console.error("Error message:", error.message);
      alert("Logout failed! Please check console for details.");
    });
  logoutModal.style.display = "none"; l
});


cancelLogout.addEventListener("click", () => {
  logoutModal.style.display = "none";
});
