/* =============================================
   GOOD MARKET — SHARED COMPONENTS JS
   ============================================= */

// SVG Icons
const ICONS = {
  logo: `<img src="${typeof getBase==='function'?getBase():''}assets/images/logo.png" alt="Good Market" style="width:36px;height:36px;border-radius:50%;object-fit:contain">`,
  search: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="9" r="6"/><path d="M14 14l4 4"/></svg>`,
  heart: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"/></svg>`,
  cart: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z"/></svg>`,
  bell: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6z"/><path d="M10 18a2 2 0 002-2H8a2 2 0 002 2z"/></svg>`,
  user: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M10 10a4 4 0 100-8 4 4 0 000 8zm0 2c-5 0-8 2.5-8 4v2h16v-2c0-1.5-3-4-8-4z"/></svg>`,
  menu: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 5h14M3 10h14M3 15h14"/></svg>`,
  globe: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="10" cy="10" r="8"/><path d="M2 10h16M10 2c2.5 3 3 5 3 8s-.5 5-3 8c-2.5-3-3-5-3-8s.5-5 3-8z"/></svg>`,
  star: `<svg viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>`,
  check: `<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>`,
  arrow: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 7l6 6M13 7v6H7"/></svg>`,
  filter: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 4h14M5 8h10M7 12h6M9 16h2"/></svg>`,
  grid: `<svg viewBox="0 0 20 20" fill="currentColor"><rect x="2" y="2" width="7" height="7" rx="1"/><rect x="11" y="2" width="7" height="7" rx="1"/><rect x="2" y="11" width="7" height="7" rx="1"/><rect x="11" y="11" width="7" height="7" rx="1"/></svg>`,
  list: `<svg viewBox="0 0 20 20" fill="currentColor"><rect x="2" y="3" width="16" height="2" rx="1"/><rect x="2" y="9" width="16" height="2" rx="1"/><rect x="2" y="15" width="16" height="2" rx="1"/></svg>`,
  map: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M10 17s-6-5.5-6-9a6 6 0 1112 0c0 3.5-6 9-6 9z"/><circle cx="10" cy="8" r="2"/></svg>`,
  plus: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 4v12M4 10h12"/></svg>`,
  edit: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13.586 3.586a2 2 0 112.828 2.828l-8.414 8.414-4 1 1-4 8.586-8.242z"/></svg>`,
  trash: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 5h12M8 5V3h4v2m-7 0v10a2 2 0 002 2h6a2 2 0 002-2V5H5z"/></svg>`,
  download: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M10 3v10m0 0l-3-3m3 3l3-3M3 15v2h14v-2"/></svg>`,
  share: `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="14" cy="4" r="2"/><circle cx="4" cy="10" r="2"/><circle cx="14" cy="16" r="2"/><path d="M6 11l6 4M6 9l6-4"/></svg>`,
};

// Determine path prefix based on current file location
function getBase() {
  const d = document.querySelector('meta[name="gm-depth"]');
  return d ? d.content : '';
}

// Render Top Navigation
function renderNav(activeLink) {
  const b = getBase();
  return `
  <nav class="topnav">
    <div class="topnav-inner">
      <a href="${b}public/home.html" class="topnav-logo"><img src="${b}assets/images/logo.png" alt="Good Market"></a>
      <div class="topnav-links">
        <a href="${b}public/home.html" class="topnav-link ${activeLink==='home'?'active':''}">Home</a>
        <a href="${b}public/marketplace.html" class="topnav-link ${activeLink==='marketplace'?'active':''}">Marketplace</a>
        <a href="${b}public/directory.html" class="topnav-link ${activeLink==='directory'?'active':''}">Directory</a>
        <a href="${b}public/networks.html" class="topnav-link ${activeLink==='networks'?'active':''}">Networks</a>
        <a href="${b}public/impact.html" class="topnav-link ${activeLink==='impact'?'active':''}">Impact</a>
        <a href="${b}public/events.html" class="topnav-link ${activeLink==='events'?'active':''}">Events</a>
        <a href="${b}public/about.html" class="topnav-link ${activeLink==='about'?'active':''}">About</a>
      </div>
      <div class="topnav-actions">
        <div class="search-bar">
          ${ICONS.search}
          <input type="text" placeholder="Search enterprises, products...">
        </div>
        <a href="${b}buyer/favorites.html" class="btn btn-icon btn-ghost" title="Favorites">${ICONS.heart}</a>
        <a href="${b}buyer/cart.html" class="btn btn-icon btn-ghost" title="Cart">${ICONS.cart}</a>
        <a href="${b}auth/login.html" class="btn btn-sm btn-secondary">Log In</a>
        <a href="${b}auth/register.html" class="btn btn-sm btn-primary">Join</a>
      </div>
    </div>
  </nav>`;
}

// Render Footer
function renderFooter() {
  const b = getBase();
  return `
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div style="margin-bottom:var(--space-4)"><img src="${b}assets/images/logo.png" alt="Good Market" style="height:48px;width:auto;object-fit:contain;filter:brightness(0) invert(1)"></div>
          <p>A curated community platform and digital commons for social enterprises, responsible businesses, and changemakers creating a better world.</p>
        </div>
        <div class="footer-col">
          <h4>Marketplace</h4>
          <a href="${b}public/marketplace.html">Browse Products</a>
          <a href="${b}public/directory.html">Enterprise Directory</a>
          <a href="${b}public/map-view.html">Map View</a>
          <a href="${b}public/categories.html">Categories</a>
          <a href="${b}public/networks.html">Networks</a>
        </div>
        <div class="footer-col">
          <h4>Get Involved</h4>
          <a href="${b}auth/register.html">Create Account</a>
          <a href="${b}seller/apply.html">Apply as Vendor</a>
          <a href="${b}public/volunteer.html">Volunteer</a>
          <a href="${b}public/donate.html">Support Us</a>
          <a href="${b}public/translate.html">Help Translate</a>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <a href="${b}public/about.html">About</a>
          <a href="${b}public/standards.html">The Rules</a>
          <a href="${b}public/blog.html">Blog</a>
          <a href="${b}public/help.html">Help Center</a>
          <a href="${b}public/contact.html">Contact</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Good Market. Digital Commons.</span>
        <div style="display:flex;gap:var(--space-6)">
          <a href="${b}public/privacy.html">Privacy</a>
          <a href="${b}public/terms.html">Terms</a>
          <a href="${b}public/accessibility.html">Accessibility</a>
        </div>
      </div>
    </div>
  </footer>`;
}

// Auto-inject nav and footer
document.addEventListener('DOMContentLoaded', () => {
  const navEl = document.getElementById('gm-nav');
  const footerEl = document.getElementById('gm-footer');
  const active = document.querySelector('meta[name="gm-active"]');
  if (navEl) navEl.innerHTML = renderNav(active ? active.content : '');
  if (footerEl) footerEl.innerHTML = renderFooter();
});
