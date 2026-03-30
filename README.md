# Good Market — Modernised UI/UX Prototype

> **Non-functional prototype** for demonstrating the redesigned Good Market platform to clients.
> 64 interconnected HTML pages covering all user flows.

## 🚀 Running the Prototype

```bash
cd "/Users/randithasenarathne/Desktop/Test Project"
python3 -m http.server 6176
```

Open **http://localhost:6176** in your browser.

## 📁 Project Structure (64 Pages)

### 🏠 Public Pages (20)
| Page | URL |
|------|-----|
| **Home / Landing** | `/public/home.html` |
| **Marketplace Browse** | `/public/marketplace.html` |
| **Product Detail** | `/public/product-detail.html` |
| **Enterprise Directory** | `/public/directory.html` |
| **Enterprise Profile** | `/public/enterprise-profile.html` |
| **Networks** | `/public/networks.html` |
| **Network Detail** | `/public/network-detail.html` |
| **Categories** | `/public/categories.html` |
| **Map View** | `/public/map-view.html` |
| **Impact Dashboard** | `/public/impact.html` |
| **Events** | `/public/events.html` |
| **Blog** | `/public/blog.html` |
| **About** | `/public/about.html` |
| **The Rules / Standards** | `/public/standards.html` |
| **Help Center** | `/public/help.html` |
| **Contact** | `/public/contact.html` |
| **Donate** | `/public/donate.html` |
| **Forum** | `/public/forum.html` |
| **Privacy Policy** | `/public/privacy.html` |
| **Terms of Service** | `/public/terms.html` |

### 🔐 Auth Pages (4)
| Page | URL |
|------|-----|
| **Login** | `/auth/login.html` |
| **Register** | `/auth/register.html` |
| **Forgot Password** | `/auth/forgot-password.html` |
| **Verify Email** | `/auth/verify-email.html` |

### 🛒 Buyer Pages (11)
| Page | URL |
|------|-----|
| **Dashboard** | `/buyer/dashboard.html` |
| **Favorites** | `/buyer/favorites.html` |
| **Cart** | `/buyer/cart.html` |
| **Checkout** | `/buyer/checkout.html` |
| **Order Confirmation** | `/buyer/order-confirmation.html` |
| **Orders List** | `/buyer/orders.html` |
| **Order Detail** | `/buyer/order-detail.html` |
| **Messages** | `/buyer/messages.html` |
| **Following** | `/buyer/following.html` |
| **Reviews** | `/buyer/reviews.html` |
| **Settings** | `/buyer/settings.html` |

### 🏪 Seller / Vendor Pages (13)
| Page | URL |
|------|-----|
| **Seller Dashboard** | `/seller/dashboard.html` |
| **My Listings** | `/seller/listings.html` |
| **Add Listing** | `/seller/add-listing.html` |
| **Edit Listing** | `/seller/edit-listing.html` |
| **Orders** | `/seller/orders.html` |
| **Order Detail** | `/seller/order-detail.html` |
| **Analytics** | `/seller/analytics.html` |
| **Edit Profile** | `/seller/profile-edit.html` |
| **Community Feedback** | `/seller/feedback.html` |
| **Networks** | `/seller/network-manage.html` |
| **Subscription Plans** | `/seller/subscription.html` |
| **Apply** | `/seller/apply.html` |
| **Settings** | `/seller/settings.html` |

### ⚙️ Admin / Backend Pages (11)
| Page | URL |
|------|-----|
| **Admin Dashboard** | `/admin/dashboard.html` |
| **Applications** | `/admin/applications.html` |
| **Application Review** | `/admin/application-review.html` |
| **Enterprises** | `/admin/enterprises.html` |
| **Users** | `/admin/users.html` |
| **Listings Review** | `/admin/listings-review.html` |
| **Reports** | `/admin/reports.html` |
| **Curation Tools** | `/admin/curation.html` |
| **Networks Admin** | `/admin/networks-admin.html` |
| **Content Management** | `/admin/content.html` |
| **Platform Settings** | `/admin/settings.html` |

### 🗂 Shared Assets
| File | Purpose |
|------|---------|
| `assets/css/design-system.css` | Complete design system (tokens, components, utilities) |
| `assets/js/components.js` | Shared navigation, footer, icons |
| `index.html` | Hub page linking to all 64 pages |

## 🎨 Design Approach

**Inspired by:** Patagonia, Etsy, Airbnb, B-Corp marketplaces

- **Typography:** DM Serif Display + Plus Jakarta Sans
- **Color:** Earthy greens, warm ambers, coral accents
- **Layout:** Clean, spacious, card-based with generous whitespace
- **Components:** Custom design system with 30+ reusable components
- **Responsive:** Mobile-first breakpoints at 640px and 1024px

## 📋 Coverage (360°)

✅ Public-facing storefront (home, marketplace, search, categories)
✅ Product discovery & detail pages with reviews
✅ Enterprise directory with profiles, levels, and certifications
✅ Network ecosystem pages
✅ Full authentication flow (login, register, forgot password, verify)
✅ Complete buyer journey (browse → cart → checkout → orders)
✅ Full seller dashboard (listings, orders, analytics, profile, feedback)
✅ Vendor application & onboarding flow
✅ Subscription & pricing tiers
✅ Admin panel (applications, curation, users, enterprises, reports)
✅ Content management & moderation tools
✅ Community features (forum, feedback, following)
✅ Informational pages (about, impact, standards, blog, events)
✅ Legal & support (privacy, terms, accessibility, help, contact)
