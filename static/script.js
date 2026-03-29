// static/script.js
console.log('Script loaded successfully');

// Sidebar Logic
function toggleNav() {
    var sidebar = document.getElementById("mySidebar");
    var main = document.querySelector('.main-content');
    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-400px";
        main.style.marginLeft = ""; 
    } else {
        sidebar.style.left = "0px";
        if (window.innerWidth > 850) main.style.marginLeft = "400px";
    }
}

function closeNav() {
    var sidebar = document.getElementById("mySidebar");
    var main = document.querySelector('.main-content');
    sidebar.style.left = "-400px";
    main.style.marginLeft = ""; 
}

// Tab Logic
function switchTab(tabName) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.form-section').forEach(sec => sec.classList.remove('active'));
    if(tabName === 'custom') {
        document.querySelectorAll('.tab-btn')[0].classList.add('active');
        document.getElementById('custom-form').classList.add('active');
    } else {
        document.querySelectorAll('.tab-btn')[1].classList.add('active');
        document.getElementById('auto-form').classList.add('active');
    }
}

// 3-Dots Dropdown
function toggleDropdown(id) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        if (dropdowns[i].id !== id) dropdowns[i].classList.remove('show');
    }
    document.getElementById(id).classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            if (dropdowns[i].classList.contains('show')) dropdowns[i].classList.remove('show');
        }
    }
};

// Loading States
document.getElementById("customNewsForm").addEventListener("submit", function() {
    let btn = document.getElementById("customBtn"); 
    btn.innerHTML = "⏳ Printing..."; 
    btn.disabled = true;
});
document.getElementById("autoNewsForm").addEventListener("submit", function() {
    let btn = document.getElementById("autoBtn"); 
    btn.innerHTML = "⏳ Working..."; 
    btn.disabled = true;
});

// PDF Downloader for Single Item
function downloadPDF(elementId, titleName) {
    let safeTitle = titleName.replace(/[^a-z0-9]/gi, '_').toLowerCase();
    var element = document.getElementById(elementId);
    var opt = {
        margin: [0.4, 0.4, 0.4, 0.4], 
        filename: 'Bakwaas_' + safeTitle + '.pdf',
        image: { type: 'jpeg', quality: 1 }, 
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
}

// 🔥 BULLETPROOF Download All PDF (this fixes the empty PDF)
function downloadAllPDF() {
    var btn = document.querySelector('button[onclick="downloadAllPDF()"]');
    var originalText = btn.innerText;

    btn.innerText = "⏳ Formatting...";
    btn.disabled = true;

    var element = document.getElementById('hidden-all-print');
    var originalDisplay = element.style.display;

    element.style.display = 'block';
    element.style.left = '-99999px';

    void element.offsetHeight;   // Force render

    console.log('📄 Starting PDF generation...');

    const images = element.querySelectorAll('img');
    let loadedCount = 0;
    const totalImages = images.length;

    let timeoutId = null;

    function checkAllLoaded() {
        if (loadedCount >= totalImages || totalImages === 0) {
            clearTimeout(timeoutId);
            console.log('✅ All images ready – generating PDF');
            generatePDF();
        }
    }

    // Give each image max 4 seconds
    if (totalImages === 0) {
        generatePDF();
    } else {
        images.forEach((img, i) => {
            if (img.complete && img.naturalHeight !== 0) {
                loadedCount++;
                checkAllLoaded();
            } else {
                img.onload = () => { loadedCount++; checkAllLoaded(); };
                img.onerror = () => { 
                    console.warn(`Image ${i+1} failed`);
                    loadedCount++; 
                    checkAllLoaded(); 
                };
            }
        });

        // Force proceed after maximum 8 seconds
        timeoutId = setTimeout(() => {
            console.warn('⏰ Timeout reached – generating PDF with available content');
            clearTimeout(timeoutId);
            generatePDF();
        }, 8000);
    }

    function generatePDF() {
        var opt = {
            margin: [0.5, 0.5, 0.5, 0.5],
            filename: 'All_Bakwaas_History.pdf',
            image: { type: 'jpeg', quality: 0.95 },
            html2canvas: { 
                scale: 2, 
                useCORS: true,
                letterRendering: true,
                scrollY: 0,
                width: 820,
                ignoreElements: (el) => el.id === 'hidden-all-print' // safety
            },
            jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' },
            pagebreak: { mode: ['css', 'legacy'] }
        };

        html2pdf().set(opt).from(element).save()
            .then(() => {
                console.log('✅ PDF Downloaded Successfully!');
                resetButton();
            })
            .catch(err => {
                console.error('❌ PDF Error:', err);
                resetButton();
            });
    }

    function resetButton() {
        element.style.display = originalDisplay;
        element.style.left = '-99999px';
        btn.innerText = originalText;
        btn.disabled = false;
    }
}