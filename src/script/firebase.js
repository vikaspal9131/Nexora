import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-auth.js";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBnrOLlosTDGHCxXKZdFrO_ev-Oy2Ruv3U",
    authDomain: "nexora-213e2.firebaseapp.com",
    projectId: "nexora-213e2",
    storageBucket: "nexora-213e2.appspot.com",
    messagingSenderId: "998457123271",
    appId: "1:998457123271:web:436292c777f2d2b29b39e2",
    measurementId: "G-V74NX09TNP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

// Get elements
const loginPage = document.querySelector("#login-page");
const loader = document.querySelector("#loader");

// Show loader initially
if (loader) loader.style.display = "block";
if (loginPage) loginPage.style.display = "none";

// Check if user is already logged in
onAuthStateChanged(auth, (user) => {
    if (user) {
        // Store login status in localStorage
        localStorage.setItem("isLoggedIn", "true");

        // Check if already on dashboard, if not, redirect
        if (window.location.pathname !== "/frontend/dashboard.html") {
            window.location.href = "/frontend/dashboard.html";
        }
    } else {
        // Remove login status if user is logged out
        localStorage.removeItem("isLoggedIn");

        // If no user, show login page and hide loader
        if (loader) loader.style.display = "none";
        if (loginPage) loginPage.style.display = "block";
    }
});

// Google Login Button
const googleBtn = document.querySelector('#google-btn');

if (googleBtn) {
    googleBtn.addEventListener("click", async () => {
        try {
            const result = await signInWithPopup(auth, provider);
            console.log("User signed in:", result.user);
            
            // Store login status
            localStorage.setItem("isLoggedIn", "true");

            // Redirect to dashboard
            window.location.href = "/frontend/dashboard.html";
        } catch (error) {
            console.error("Login Error:", error.message);
        }
    });
}
