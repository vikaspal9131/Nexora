import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-analytics.js";
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
const analytics = getAnalytics(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

// Google Login Button
const googleBtn = document.querySelector('#google-btn');

googleBtn.addEventListener("click", async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        console.log("User signed in:", result.user);
        window.location.href = "/frontend/dashboard.html";
    } catch (error) {
        console.error("Login Error:", error.message);
    }
});

onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log("User logged in:", user);
        updateUserProfile(user);
    } else {
        console.log("No user is signed in.");
    }
});


function updateUserProfile(user) {
    const photo = document.querySelector('#userPhoto'); // Correct ID
    if (photo) {
        if (user.photoURL) {
            photo.src = user.photoURL;
            console.log("Profile photo updated:", user.photoURL);
        } else {
            console.warn("User photo not available. Setting default avatar.");
            photo.src = "./assets/images/del1.webp"; // Default image path
        }
    } else {
        console.warn("Profile image element not found!");
    }
}





 



