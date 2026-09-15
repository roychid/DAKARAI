// Alternate a subtle background tint between sections for visual
// separation, replacing the divider lines that used to do this job.
document.querySelectorAll('main .section').forEach((section, i) => {
  if (i % 2 === 1) section.classList.add('section-tint');
});

// Mobile nav toggle
const navToggle = document.getElementById('navToggle');
const nav = document.getElementById('nav');
const navBackdrop = document.getElementById('navBackdrop');

function openNav() {
  nav.classList.add('open');
  navToggle.classList.add('open');
  navToggle.setAttribute('aria-expanded', 'true');
  navToggle.setAttribute('aria-label', 'Close menu');
  navBackdrop.classList.add('visible');
}

function closeNav() {
  nav.classList.remove('open');
  navToggle.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
  navToggle.setAttribute('aria-label', 'Open menu');
  navBackdrop.classList.remove('visible');
}

if (navToggle) {
  navToggle.addEventListener('click', () => {
    nav.classList.contains('open') ? closeNav() : openNav();
  });
}

// Close nav when a link is clicked
document.querySelectorAll('.nav a').forEach(link => {
  link.addEventListener('click', closeNav);
});

// Close nav when tapping outside it
if (navBackdrop) {
  navBackdrop.addEventListener('click', closeNav);
}

// Close nav on Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeNav();
});

// Subtle fade-in on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('section').forEach(section => {
  section.classList.add('fade-in');
  observer.observe(section);
});
