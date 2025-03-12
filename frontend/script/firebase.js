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
        window.location.href = "/";
    } catch (error) {
        console.error("Login Error:", error.message);
    }
});

// Check user login state
onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log("User logged in:", user);
        updateUserProfile(user);
    } else {
        console.log("No user is signed in.");
    }
});

// Update user profile function
function updateUserProfile(user) {
    if (user) {
        const profilePhoto = user.photoURL;
        const photo = document.querySelector('#user-profile');
        if (photo) {
            photo.src = profilePhoto;
        }
    }
}
