#!/usr/bin/env python3
"""Generate all remaining Good Market UI pages"""
import os

BASE = "/Users/randithasenarathne/Desktop/Test Project"

def head(title, depth="../", active=""):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="gm-depth" content="{depth}"><meta name="gm-active" content="{active}"><title>{title} — Good Market</title><link rel="stylesheet" href="{depth}assets/css/design-system.css"></head>'''

def foot(depth="../"):
    return f'<div id="gm-footer"></div><script src="{depth}assets/js/components.js"></script></body></html>'

def seller_sidebar(active_page):
    links = [("dashboard.html","📊 Dashboard"),("listings.html","📦 My Listings"),("add-listing.html","➕ Add Listing"),("orders.html","🛒 Orders"),("analytics.html","📈 Analytics"),("profile-edit.html","✏️ Edit Profile"),("feedback.html","⭐ Feedback"),("network-manage.html","🌐 Networks"),("subscription.html","💳 Subscription"),("apply.html","📋 Application"),("settings.html","⚙️ Settings")]
    items = "".join([f'<a href="{l[0]}" class="sell-link{"  active" if l[0]==active_page else ""}">{l[1]}</a>' for l in links])
    return f'''<aside style="width:260px;background:#fff;border-right:1px solid var(--gm-earth-200);min-height:calc(100vh - 72px);padding:24px 0;position:sticky;top:72px;flex-shrink:0"><div style="display:flex;align-items:center;gap:12px;padding:16px 20px 20px;border-bottom:1px solid var(--gm-earth-100);margin-bottom:16px"><div style="width:40px;height:40px;border-radius:8px;background:var(--gm-green-100);display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--gm-green-700);font-size:14px">GH</div><div><strong style="font-size:14px">Green Harvest</strong><p style="font-size:11px;color:var(--gm-earth-500)">Enterprise Account</p></div></div>{items}</aside>'''

def buyer_sidebar(active_page):
    links = [("dashboard.html","📊 Dashboard"),("favorites.html","♡ Favorites"),("orders.html","📦 My Orders"),("cart.html","🛒 Cart"),("messages.html","💬 Messages"),("following.html","👥 Following"),("reviews.html","⭐ My Reviews"),("settings.html","⚙️ Settings")]
    items = "".join([f'<a href="{l[0]}" style="display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:{"var(--gm-green-700)" if l[0]==active_page else "var(--gm-earth-600)"};text-decoration:none;{"background:var(--gm-green-50);font-weight:600;border-left:3px solid var(--gm-green-500)" if l[0]==active_page else ""}">{l[1]}</a>' for l in links])
    return f'''<aside style="width:260px;background:#fff;border-right:1px solid var(--gm-earth-200);min-height:calc(100vh - 72px);padding:24px 0;position:sticky;top:72px;flex-shrink:0"><div style="display:flex;align-items:center;gap:12px;padding:0 20px 20px;border-bottom:1px solid var(--gm-earth-100);margin-bottom:16px"><div style="width:40px;height:40px;border-radius:50%;background:var(--gm-green-200);display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--gm-green-800)">JD</div><div><strong style="font-size:14px">John Doe</strong><p style="font-size:11px;color:var(--gm-earth-500)">Personal Account</p></div></div>{items}</aside>'''

def admin_sidebar(active_page):
    links = [("dashboard.html","📊 Dashboard"),("applications.html","📋 Applications"),("enterprises.html","🏢 Enterprises"),("users.html","👥 Users"),("listings-review.html","📦 Listings"),("reports.html","📈 Reports"),("curation.html","✅ Curation"),("networks-admin.html","🌐 Networks"),("content.html","📝 Content"),("settings.html","⚙️ Settings")]
    items = "".join([f'<a href="{l[0]}" style="display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:{"var(--gm-green-700)" if l[0]==active_page else "var(--gm-earth-600)"};text-decoration:none;{"background:var(--gm-green-50);font-weight:600;border-left:3px solid var(--gm-green-500)" if l[0]==active_page else ""}">{l[1]}</a>' for l in links])
    return f'''<aside style="width:260px;background:var(--gm-earth-900);min-height:calc(100vh - 72px);padding:24px 0;position:sticky;top:72px;flex-shrink:0"><div style="padding:0 20px 20px;border-bottom:1px solid var(--gm-earth-700);margin-bottom:16px"><div style="font-family:var(--font-display);font-size:18px;color:#fff;margin-bottom:4px">Admin Panel</div><p style="font-size:11px;color:var(--gm-earth-400)">Good Market Platform</p></div>{items.replace("var(--gm-earth-600)","var(--gm-earth-400)").replace("var(--gm-green-50)","rgba(32,169,106,.1)").replace("var(--gm-green-500)","var(--gm-green-400)").replace("var(--gm-green-700)","var(--gm-green-400)")}</aside>'''

pages = {}

# ========== SELLER PAGES ==========
pages["seller/listings.html"] = f'''{head("My Listings")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none;transition:all .15s}}.sell-link:hover{{background:var(--gm-green-50);color:var(--gm-green-700)}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}.listing-row{{display:flex;align-items:center;gap:16px;padding:16px;background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);margin-bottom:12px;transition:all .2s}}.listing-row:hover{{box-shadow:var(--shadow-md);border-color:var(--gm-green-200)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("listings.html")}
<main class="page-content">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:32px"><div><h1 class="page-title">My Listings</h1><p class="page-subtitle">Manage your marketplace products and services</p></div><a href="add-listing.html" class="btn btn-primary btn-sm">+ Add New Listing</a></div>
  <div class="tabs" style="margin-bottom:24px"><a class="tab active">All (12)</a><a class="tab">Published (10)</a><a class="tab">Draft (1)</a><a class="tab">Pending Review (1)</a></div>
  <div class="listing-row"><img src="https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=80&h=80&fit=crop" style="width:64px;height:64px;border-radius:8px;object-fit:cover" alt=""><div style="flex:1"><div style="display:flex;justify-content:space-between"><div><strong style="font-size:14px">True Ceylon Cinnamon Sticks — 100g</strong><p style="font-size:12px;color:var(--gm-earth-500)">Food & Beverages • Shop (B2C)</p></div><div style="text-align:right"><strong style="color:var(--gm-green-700)">$12.50</strong><p style="font-size:11px;color:var(--gm-earth-500)">48 sold</p></div></div><div style="display:flex;gap:8px;margin-top:8px"><span class="badge badge-green">Published</span><a href="edit-listing.html" class="btn btn-sm btn-ghost">Edit</a><button class="btn btn-sm btn-ghost" style="color:var(--gm-coral-500)">Unpublish</button></div></div></div>
  <div class="listing-row"><img src="https://images.unsplash.com/photo-1607004468138-e7e23ea26947?w=80&h=80&fit=crop" style="width:64px;height:64px;border-radius:8px;object-fit:cover" alt=""><div style="flex:1"><div style="display:flex;justify-content:space-between"><div><strong style="font-size:14px">Organic Black Pepper — 50g</strong><p style="font-size:12px;color:var(--gm-earth-500)">Food & Beverages • Shop (B2C)</p></div><div style="text-align:right"><strong style="color:var(--gm-green-700)">$9.00</strong><p style="font-size:11px;color:var(--gm-earth-500)">32 sold</p></div></div><div style="display:flex;gap:8px;margin-top:8px"><span class="badge badge-green">Published</span><a href="edit-listing.html" class="btn btn-sm btn-ghost">Edit</a></div></div></div>
  <div class="listing-row"><img src="https://images.unsplash.com/photo-1587049352851-8d4e89133924?w=80&h=80&fit=crop" style="width:64px;height:64px;border-radius:8px;object-fit:cover" alt=""><div style="flex:1"><div style="display:flex;justify-content:space-between"><div><strong style="font-size:14px">Whole Cloves — 50g</strong><p style="font-size:12px;color:var(--gm-earth-500)">Food & Beverages • Shop (B2C)</p></div><div style="text-align:right"><strong style="color:var(--gm-green-700)">$7.25</strong><p style="font-size:11px;color:var(--gm-earth-500)">15 sold</p></div></div><div style="display:flex;gap:8px;margin-top:8px"><span class="badge badge-amber">Pending Review</span><a href="edit-listing.html" class="btn btn-sm btn-ghost">Edit</a></div></div></div>
  <div class="listing-row" style="opacity:.6"><img src="https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=80&h=80&fit=crop" style="width:64px;height:64px;border-radius:8px;object-fit:cover" alt=""><div style="flex:1"><div style="display:flex;justify-content:space-between"><div><strong style="font-size:14px">Cardamom Pods — 30g</strong><p style="font-size:12px;color:var(--gm-earth-500)">Food & Beverages • Shop (B2C)</p></div><div style="text-align:right"><strong style="color:var(--gm-earth-500)">$14.00</strong></div></div><div style="display:flex;gap:8px;margin-top:8px"><span class="badge badge-earth">Draft</span><a href="edit-listing.html" class="btn btn-sm btn-ghost">Edit</a><button class="btn btn-sm btn-primary">Publish</button></div></div></div>
</main></div>{foot()}'''

pages["seller/add-listing.html"] = f'''{head("Add Listing")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}.upload-zone{{border:2px dashed var(--gm-earth-300);border-radius:var(--radius-lg);padding:40px;text-align:center;cursor:pointer;transition:all .2s}}.upload-zone:hover{{border-color:var(--gm-green-400);background:var(--gm-green-50)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("add-listing.html")}
<main class="page-content">
  <h1 class="page-title">Add New Listing</h1><p class="page-subtitle" style="margin-bottom:32px">Create a marketplace listing for your product, service, event, or campaign</p>
  <div style="max-width:720px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Listing Type</h3>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">
        <div style="padding:16px;border:2px solid var(--gm-green-500);border-radius:var(--radius-md);text-align:center;background:var(--gm-green-50);cursor:pointer"><div style="font-size:24px;margin-bottom:4px">🛍</div><strong style="font-size:13px">Product</strong></div>
        <div style="padding:16px;border:2px solid var(--gm-earth-200);border-radius:var(--radius-md);text-align:center;cursor:pointer"><div style="font-size:24px;margin-bottom:4px">🔧</div><strong style="font-size:13px">Service</strong></div>
        <div style="padding:16px;border:2px solid var(--gm-earth-200);border-radius:var(--radius-md);text-align:center;cursor:pointer"><div style="font-size:24px;margin-bottom:4px">📅</div><strong style="font-size:13px">Event</strong></div>
        <div style="padding:16px;border:2px solid var(--gm-earth-200);border-radius:var(--radius-md);text-align:center;cursor:pointer"><div style="font-size:24px;margin-bottom:4px">📢</div><strong style="font-size:13px">Campaign</strong></div>
      </div>
    </div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Basic Information</h3>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Title</label><input class="form-input" placeholder="E.g. True Ceylon Cinnamon Sticks — 100g"></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Category</label><select class="form-select" style="width:100%"><option>Select category</option><option>Shop (B2C)</option><option>Source (B2B)</option></select></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><div class="form-group"><label class="form-label">Price (USD)</label><input class="form-input" type="number" placeholder="0.00"></div><div class="form-group"><label class="form-label">Stock Quantity</label><input class="form-input" type="number" placeholder="100"></div></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Description</label><textarea class="form-textarea" rows="4" placeholder="Describe your product, including how it meets minimum standards and how people and the planet are prioritized..."></textarea></div>
      <div class="form-group"><label class="form-label">Keywords</label><input class="form-input" placeholder="organic, cinnamon, sri lanka, fair trade"></div>
    </div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Images</h3>
      <div class="upload-zone"><div style="font-size:36px;margin-bottom:8px">📸</div><p style="font-size:14px;color:var(--gm-earth-600);margin-bottom:4px">Drop images here or click to upload</p><p style="font-size:12px;color:var(--gm-earth-400)">Square format recommended • Max 5 images • JPG, PNG</p></div>
    </div>
    <div style="display:flex;gap:12px;justify-content:flex-end"><button class="btn btn-secondary">Save as Draft</button><button class="btn btn-primary">Publish Listing</button></div>
  </div>
</main></div>{foot()}'''

pages["seller/orders.html"] = f'''{head("Seller Orders")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("orders.html")}
<main class="page-content">
  <h1 class="page-title">Orders</h1><p class="page-subtitle" style="margin-bottom:32px">Manage incoming customer orders</p>
  <div class="tabs" style="margin-bottom:24px"><a class="tab active">All Orders (156)</a><a class="tab">Pending (8)</a><a class="tab">Processing (12)</a><a class="tab">Shipped (28)</a><a class="tab">Delivered (108)</a></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);overflow:hidden">
    <table class="data-table"><thead><tr><th>Order ID</th><th>Customer</th><th>Items</th><th>Total</th><th>Status</th><th>Date</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td><strong>#GM-4821</strong></td><td>Jane Doe</td><td>Ceylon Cinnamon × 2</td><td>$25.00</td><td><span class="badge badge-green">Shipped</span></td><td>Mar 16</td><td><a href="order-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
      <tr><td><strong>#GM-4819</strong></td><td>Marco Polo</td><td>Black Pepper × 3</td><td>$27.00</td><td><span class="badge badge-amber">Processing</span></td><td>Mar 15</td><td><a href="order-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
      <tr><td><strong>#GM-4815</strong></td><td>Sarah Kim</td><td>Cinnamon + Cloves</td><td>$19.75</td><td><span class="badge badge-sky">Pending</span></td><td>Mar 14</td><td><a href="order-detail.html" class="btn btn-sm btn-primary">Process</a></td></tr>
      <tr><td><strong>#GM-4810</strong></td><td>Ahmed Rashid</td><td>Bulk Cinnamon 1kg</td><td>$89.00</td><td><span class="badge badge-green">Delivered</span></td><td>Mar 12</td><td><a href="order-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
      <tr><td><strong>#GM-4802</strong></td><td>Lisa Chen</td><td>Cardamom × 5</td><td>$70.00</td><td><span class="badge badge-green">Delivered</span></td><td>Mar 10</td><td><a href="order-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    </tbody></table>
  </div>
  <div style="display:flex;justify-content:center;gap:8px;margin-top:24px"><button class="btn btn-ghost btn-sm" disabled>← Prev</button><button class="btn btn-sm btn-primary">1</button><button class="btn btn-sm btn-ghost">2</button><button class="btn btn-sm btn-ghost">3</button><button class="btn btn-sm btn-ghost">Next →</button></div>
</main></div>{foot()}'''

pages["seller/analytics.html"] = f'''{head("Analytics")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}.chart-ph{{background:var(--gm-earth-50);border:2px dashed var(--gm-earth-200);border-radius:var(--radius-lg);height:280px;display:flex;align-items:center;justify-content:center;color:var(--gm-earth-400);font-size:14px}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("analytics.html")}
<main class="page-content">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:32px"><div><h1 class="page-title">Analytics</h1><p class="page-subtitle">Insights into your enterprise performance</p></div><select class="form-select" style="padding:8px 16px;font-size:13px"><option>Last 30 days</option><option>Last 90 days</option><option>This year</option><option>All time</option></select></div>
  <div class="grid grid-4 gap-4" style="margin-bottom:32px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500);margin-bottom:4px">Total Revenue</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">$12,480</div><div style="font-size:12px;color:var(--gm-green-600);margin-top:4px">↑ 18% vs previous period</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500);margin-bottom:4px">Total Orders</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">156</div><div style="font-size:12px;color:var(--gm-green-600);margin-top:4px">↑ 12% vs previous period</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500);margin-bottom:4px">Profile Views</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">2,340</div><div style="font-size:12px;color:var(--gm-green-600);margin-top:4px">↑ 24% vs previous period</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500);margin-bottom:4px">Conversion Rate</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">6.7%</div><div style="font-size:12px;color:var(--gm-green-600);margin-top:4px">↑ 1.2% vs previous period</div></div>
  </div>
  <div class="grid grid-2 gap-6" style="margin-bottom:32px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Revenue Over Time</h3><div class="chart-ph">📊 Revenue line chart renders here</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Top Products</h3><div class="chart-ph">📊 Product bar chart renders here</div></div>
  </div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Customer Geography</h3><div class="chart-ph" style="height:320px">🗺 Customer location map renders here</div></div>
</main></div>{foot()}'''

pages["seller/profile-edit.html"] = f'''{head("Edit Profile")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}.upload-zone{{border:2px dashed var(--gm-earth-300);border-radius:var(--radius-lg);padding:24px;text-align:center;cursor:pointer}}.upload-zone:hover{{border-color:var(--gm-green-400);background:var(--gm-green-50)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("profile-edit.html")}
<main class="page-content"><h1 class="page-title">Edit Enterprise Profile</h1><p class="page-subtitle" style="margin-bottom:32px">Update your public profile information</p>
  <div style="max-width:720px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Profile Photo & Cover</h3>
      <div style="display:flex;gap:20px;align-items:center;margin-bottom:16px"><div style="width:80px;height:80px;border-radius:var(--radius-lg);background:var(--gm-green-100);display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:var(--gm-green-700)">GH</div><div><button class="btn btn-sm btn-secondary">Change Logo</button><p style="font-size:11px;color:var(--gm-earth-400);margin-top:4px">Square image, min 200×200px</p></div></div>
      <div class="upload-zone"><p style="font-size:13px;color:var(--gm-earth-500)">📸 Upload cover image (1200×300px recommended)</p></div>
    </div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Enterprise Details</h3>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Enterprise Name</label><input class="form-input" value="Green Harvest Organics"></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Sector(s)</label><div style="display:flex;gap:6px;flex-wrap:wrap"><span class="tag">Food & Beverages ✕</span><span class="tag">Agriculture ✕</span><button class="btn btn-sm btn-ghost">+ Add sector</button></div></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Description</label><textarea class="form-textarea" rows="5">Green Harvest Organics is a family-run organic farm cooperative based in Ratnapura, Sri Lanka. We cultivate premium cinnamon, pepper, cloves, and cardamom using traditional methods passed down through generations.</textarea></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><div class="form-group"><label class="form-label">Email</label><input class="form-input" value="hello@greenharvestorganics.lk"></div><div class="form-group"><label class="form-label">Phone</label><input class="form-input" value="+94 77 123 4567"></div></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Website</label><input class="form-input" value="https://www.greenharvestorganics.lk"></div>
      <div class="form-group"><label class="form-label">Location</label><input class="form-input" value="45 Temple Road, Ratnapura, Sri Lanka"></div>
    </div>
    <div style="display:flex;gap:12px;justify-content:flex-end"><button class="btn btn-secondary">Cancel</button><button class="btn btn-primary">Save & Publish</button></div>
  </div>
</main></div>{foot()}'''

pages["seller/apply.html"] = f'''{head("Apply")}
<style>.step-indicator{{display:flex;justify-content:center;gap:0;margin-bottom:40px}}.step{{display:flex;align-items:center;gap:8px}}.step-num{{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;border:2px solid var(--gm-earth-300);color:var(--gm-earth-400)}}.step.active .step-num{{background:var(--gm-green-600);color:#fff;border-color:var(--gm-green-600)}}.step.done .step-num{{background:var(--gm-green-100);color:var(--gm-green-700);border-color:var(--gm-green-300)}}.step-line{{width:60px;height:2px;background:var(--gm-earth-200);margin:0 8px}}.step-line.active{{background:var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div>
<div style="max-width:720px;margin:0 auto;padding:40px 24px">
  <h1 style="font-size:28px;text-align:center;margin-bottom:8px">Apply to Good Market</h1>
  <p style="text-align:center;color:var(--gm-earth-500);margin-bottom:32px">Complete the application to get approved and join the community</p>
  <div class="step-indicator"><div class="step done"><span class="step-num">✓</span><span style="font-size:13px;font-weight:500">Account</span></div><div class="step-line active"></div><div class="step active"><span class="step-num">2</span><span style="font-size:13px;font-weight:500">Enterprise Info</span></div><div class="step-line"></div><div class="step"><span class="step-num">3</span><span style="font-size:13px;font-weight:500">Standards</span></div><div class="step-line"></div><div class="step"><span class="step-num">4</span><span style="font-size:13px;font-weight:500">Review</span></div></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:32px;margin-bottom:24px">
    <h3 style="font-size:18px;margin-bottom:20px">Enterprise Information</h3>
    <div class="form-group" style="margin-bottom:16px"><label class="form-label">Enterprise Name *</label><input class="form-input" placeholder="Your enterprise or organization name"></div>
    <div class="form-group" style="margin-bottom:16px"><label class="form-label">Enterprise Type *</label><select class="form-select" style="width:100%"><option>Select type</option><option>Social Enterprise</option><option>Cooperative</option><option>Responsible Business</option><option>Civic Organization</option><option>Voluntary Initiative</option><option>Network</option></select></div>
    <div class="form-group" style="margin-bottom:16px"><label class="form-label">Sector(s) *</label><select class="form-select" style="width:100%"><option>Select primary sector</option><option>Food & Beverages</option><option>Fashion & Textiles</option><option>Health & Wellness</option><option>Arts & Crafts</option><option>Agriculture</option><option>Technology</option><option>Education</option><option>Tourism</option></select></div>
    <div class="form-group" style="margin-bottom:16px"><label class="form-label">Country *</label><select class="form-select" style="width:100%"><option>Select country</option><option>Sri Lanka</option><option>India</option><option>Kenya</option></select></div>
    <div class="form-group" style="margin-bottom:16px"><label class="form-label">Description *</label><textarea class="form-textarea" rows="4" placeholder="Describe your enterprise, what you do, and how you prioritize people and planet..."></textarea></div>
    <div class="form-group"><label class="form-label">Website (optional)</label><input class="form-input" placeholder="https://"></div>
  </div>
  <div style="background:var(--gm-green-50);border-radius:var(--radius-lg);padding:20px;margin-bottom:24px;font-size:13px;color:var(--gm-earth-600)"><strong style="color:var(--gm-green-800)">💡 Tip:</strong> Applicants are never "rejected." If your application needs improvements, the curation team will provide guidance. Focus on how your enterprise meets minimum standards.</div>
  <div style="display:flex;justify-content:space-between"><button class="btn btn-secondary">← Previous</button><button class="btn btn-primary">Continue →</button></div>
</div>{foot()}'''

pages["seller/feedback.html"] = f'''{head("Feedback")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("feedback.html")}
<main class="page-content"><h1 class="page-title">Community Feedback</h1><p class="page-subtitle" style="margin-bottom:32px">Reviews and feedback from the community</p>
  <div class="grid grid-3 gap-4" style="margin-bottom:32px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px;text-align:center"><div style="font-family:var(--font-display);font-size:40px;color:var(--gm-green-600)">4.9</div><div style="color:var(--gm-amber-400);margin:4px 0">★★★★★</div><div style="font-size:13px;color:var(--gm-earth-500)">48 reviews</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><div style="font-size:13px;margin-bottom:8px">Rating distribution</div><div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><span style="font-size:12px;width:16px">5</span><div style="flex:1;height:8px;background:var(--gm-earth-100);border-radius:4px;overflow:hidden"><div style="width:85%;height:100%;background:var(--gm-green-500);border-radius:4px"></div></div><span style="font-size:11px;color:var(--gm-earth-400)">41</span></div><div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><span style="font-size:12px;width:16px">4</span><div style="flex:1;height:8px;background:var(--gm-earth-100);border-radius:4px;overflow:hidden"><div style="width:10%;height:100%;background:var(--gm-green-400);border-radius:4px"></div></div><span style="font-size:11px;color:var(--gm-earth-400)">5</span></div><div style="display:flex;align-items:center;gap:8px"><span style="font-size:12px;width:16px">3</span><div style="flex:1;height:8px;background:var(--gm-earth-100);border-radius:4px;overflow:hidden"><div style="width:4%;height:100%;background:var(--gm-amber-400);border-radius:4px"></div></div><span style="font-size:11px;color:var(--gm-earth-400)">2</span></div></div>
    <div style="background:var(--gm-green-50);border:1px solid var(--gm-green-200);border-radius:var(--radius-lg);padding:24px"><div style="font-size:14px;font-weight:600;color:var(--gm-green-800);margin-bottom:8px">💡 Feedback Tips</div><p style="font-size:13px;color:var(--gm-earth-600);line-height:1.6">Reply to reviews promptly. Positive engagement builds trust and attracts more customers.</p></div>
  </div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px">
    <div style="padding:16px 0;border-bottom:1px solid var(--gm-earth-100)"><div style="display:flex;justify-content:space-between;margin-bottom:8px"><div style="display:flex;align-items:center;gap:8px"><div style="width:32px;height:32px;border-radius:50%;background:var(--gm-sky-100);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:var(--gm-sky-600)">JD</div><strong style="font-size:13px">Jane Doe</strong><span style="font-size:11px;color:var(--gm-earth-400)">2 weeks ago</span></div><span style="color:var(--gm-amber-400)">★★★★★</span></div><p style="font-size:13px;color:var(--gm-earth-600)">The best cinnamon I have ever tasted. Packaging was plastic-free which I loved.</p><button class="btn btn-sm btn-ghost" style="margin-top:8px">Reply</button></div>
    <div style="padding:16px 0"><div style="display:flex;justify-content:space-between;margin-bottom:8px"><div style="display:flex;align-items:center;gap:8px"><div style="width:32px;height:32px;border-radius:50%;background:var(--gm-amber-100);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:var(--gm-amber-600)">MP</div><strong style="font-size:13px">Marco P.</strong><span style="font-size:11px;color:var(--gm-earth-400)">1 month ago</span></div><span style="color:var(--gm-amber-400)">★★★★☆</span></div><p style="font-size:13px;color:var(--gm-earth-600)">Good quality. Shipping a bit slow but product was worth the wait.</p><div style="margin-left:40px;margin-top:12px;padding:12px;background:var(--gm-green-50);border-radius:var(--radius-md);font-size:13px"><strong style="color:var(--gm-green-700)">Green Harvest replied:</strong><p style="color:var(--gm-earth-600);margin-top:4px">Thank you Marco! We are working on faster international shipping options.</p></div></div>
  </div>
</main></div>{foot()}'''

pages["seller/subscription.html"] = f'''{head("Subscription")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}.plan-card{{background:#fff;border:2px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;transition:all .2s}}.plan-card:hover{{border-color:var(--gm-green-300);transform:translateY(-4px);box-shadow:var(--shadow-lg)}}.plan-card.recommended{{border-color:var(--gm-green-500);position:relative}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("subscription.html")}
<main class="page-content"><h1 class="page-title">Subscription Plans</h1><p class="page-subtitle" style="margin-bottom:32px">It is free to be Good Market approved. Premium plans unlock additional features.</p>
  <div style="display:flex;gap:8px;margin-bottom:32px"><span class="badge badge-green" style="font-size:13px;padding:6px 14px">Your plan: Free</span></div>
  <div class="grid grid-3 gap-6">
    <div class="plan-card"><h3 style="font-size:20px;margin-bottom:4px">Free</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:20px">Always free</p><div style="font-family:var(--font-display);font-size:36px;margin-bottom:20px">$0<span style="font-size:14px;font-family:var(--font-body);color:var(--gm-earth-400)">/month</span></div><div style="text-align:left;font-size:13px;color:var(--gm-earth-600);display:flex;flex-direction:column;gap:8px;margin-bottom:24px"><div>✅ Public profile</div><div>✅ 5 basic listings</div><div>✅ Community feedback</div><div>✅ Good Market Approved badge</div><div style="color:var(--gm-earth-400)">✗ Cart listings</div><div style="color:var(--gm-earth-400)">✗ Analytics dashboard</div></div><button class="btn btn-secondary" style="width:100%" disabled>Current Plan</button></div>
    <div class="plan-card recommended"><div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%)"><span class="badge badge-green" style="font-size:11px">Recommended</span></div><h3 style="font-size:20px;margin-bottom:4px">Growth</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:20px">For growing enterprises</p><div style="font-family:var(--font-display);font-size:36px;margin-bottom:20px">$19<span style="font-size:14px;font-family:var(--font-body);color:var(--gm-earth-400)">/month</span></div><div style="text-align:left;font-size:13px;color:var(--gm-earth-600);display:flex;flex-direction:column;gap:8px;margin-bottom:24px"><div>✅ Everything in Free</div><div>✅ Unlimited listings</div><div>✅ Cart listings (sell online)</div><div>✅ Analytics dashboard</div><div>✅ Priority in search</div><div style="color:var(--gm-earth-400)">✗ API access</div></div><button class="btn btn-primary" style="width:100%">Upgrade to Growth</button></div>
    <div class="plan-card"><h3 style="font-size:20px;margin-bottom:4px">Pro</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:20px">For established enterprises</p><div style="font-family:var(--font-display);font-size:36px;margin-bottom:20px">$49<span style="font-size:14px;font-family:var(--font-body);color:var(--gm-earth-400)">/month</span></div><div style="text-align:left;font-size:13px;color:var(--gm-earth-600);display:flex;flex-direction:column;gap:8px;margin-bottom:24px"><div>✅ Everything in Growth</div><div>✅ API access</div><div>✅ Advanced analytics</div><div>✅ Custom branding</div><div>✅ Priority support</div><div>✅ Network management</div></div><button class="btn btn-secondary" style="width:100%">Upgrade to Pro</button></div>
  </div>
</main></div>{foot()}'''

# ========== ADMIN PAGES ==========
pages["admin/dashboard.html"] = f'''{head("Admin Dashboard")}
<style>a{{text-decoration:none}}.admin-metric{{background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px}}.admin-metric-val{{font-family:var(--font-display);font-size:32px;color:var(--gm-green-600)}}.admin-metric-label{{font-size:13px;color:var(--gm-earth-500);margin-top:4px}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("dashboard.html")}
<main class="page-content">
  <h1 class="page-title">Admin Dashboard</h1><p class="page-subtitle" style="margin-bottom:32px">Platform overview and moderation tools</p>
  <div class="grid grid-4 gap-4" style="margin-bottom:32px">
    <div class="admin-metric"><div class="admin-metric-val">4,832</div><div class="admin-metric-label">Total Enterprises</div></div>
    <div class="admin-metric"><div class="admin-metric-val">15,240</div><div class="admin-metric-label">Total Users</div></div>
    <div class="admin-metric"><div class="admin-metric-val">23</div><div class="admin-metric-label">Pending Applications</div></div>
    <div class="admin-metric"><div class="admin-metric-val">12</div><div class="admin-metric-label">Flagged Content</div></div>
  </div>
  <div class="grid grid-2 gap-6" style="margin-bottom:32px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Recent Applications</h3>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--gm-earth-100)"><div><strong style="font-size:13px">Eco Bloom Gardens</strong><p style="font-size:11px;color:var(--gm-earth-500)">Agriculture • Kenya</p></div><div style="display:flex;gap:6px"><a href="applications.html" class="btn btn-sm btn-primary">Review</a></div></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--gm-earth-100)"><div><strong style="font-size:13px">Urban Threads Co.</strong><p style="font-size:11px;color:var(--gm-earth-500)">Fashion • India</p></div><div style="display:flex;gap:6px"><a href="applications.html" class="btn btn-sm btn-primary">Review</a></div></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0"><div><strong style="font-size:13px">SolarPower Hub</strong><p style="font-size:11px;color:var(--gm-earth-500)">Technology • Ghana</p></div><div style="display:flex;gap:6px"><a href="applications.html" class="btn btn-sm btn-primary">Review</a></div></div>
      </div><a href="applications.html" style="display:block;text-align:center;margin-top:12px;font-size:13px">View all 23 applications →</a>
    </div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px">
      <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Flagged Content</h3>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--gm-earth-100)"><div><strong style="font-size:13px">Listing: "Organic" claims unverified</strong><p style="font-size:11px;color:var(--gm-earth-500)">Reported by community member</p></div><span class="badge badge-coral">Urgent</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--gm-earth-100)"><div><strong style="font-size:13px">Review: Inappropriate language</strong><p style="font-size:11px;color:var(--gm-earth-500)">Auto-detected</p></div><span class="badge badge-amber">Medium</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0"><div><strong style="font-size:13px">Profile: Outdated contact info</strong><p style="font-size:11px;color:var(--gm-earth-500)">Community report</p></div><span class="badge badge-sky">Low</span></div>
      </div>
    </div>
  </div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px">
    <h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Platform Activity — Last 30 Days</h3>
    <div style="background:var(--gm-earth-50);border:2px dashed var(--gm-earth-200);border-radius:var(--radius-lg);height:280px;display:flex;align-items:center;justify-content:center;color:var(--gm-earth-400)">📊 Platform activity chart renders here</div>
  </div>
</main></div>{foot()}'''

pages["admin/applications.html"] = f'''{head("Applications Review")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("applications.html")}
<main class="page-content"><h1 class="page-title">Applications</h1><p class="page-subtitle" style="margin-bottom:32px">Review and process enterprise applications</p>
  <div class="tabs" style="margin-bottom:24px"><a class="tab active">Pending (23)</a><a class="tab">Under Review (8)</a><a class="tab">Approved (4,741)</a><a class="tab">Needs Improvement (60)</a></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);overflow:hidden">
    <table class="data-table"><thead><tr><th>Enterprise</th><th>Sector</th><th>Country</th><th>Submitted</th><th>Status</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td><strong>Eco Bloom Gardens</strong></td><td>Agriculture</td><td>Kenya</td><td>Mar 16, 2026</td><td><span class="badge badge-amber">Pending</span></td><td><a href="application-review.html" class="btn btn-sm btn-primary">Review</a></td></tr>
      <tr><td><strong>Urban Threads Co.</strong></td><td>Fashion</td><td>India</td><td>Mar 15, 2026</td><td><span class="badge badge-amber">Pending</span></td><td><a href="application-review.html" class="btn btn-sm btn-primary">Review</a></td></tr>
      <tr><td><strong>SolarPower Hub</strong></td><td>Technology</td><td>Ghana</td><td>Mar 14, 2026</td><td><span class="badge badge-sky">Under Review</span></td><td><a href="application-review.html" class="btn btn-sm btn-ghost">Continue</a></td></tr>
      <tr><td><strong>Pacific Kelp Farm</strong></td><td>Food</td><td>New Zealand</td><td>Mar 13, 2026</td><td><span class="badge badge-amber">Pending</span></td><td><a href="application-review.html" class="btn btn-sm btn-primary">Review</a></td></tr>
      <tr><td><strong>Bamboo Works</strong></td><td>Crafts</td><td>Vietnam</td><td>Mar 12, 2026</td><td><span class="badge badge-amber">Pending</span></td><td><a href="application-review.html" class="btn btn-sm btn-primary">Review</a></td></tr>
    </tbody></table>
  </div>
</main></div>{foot()}'''

pages["admin/application-review.html"] = f'''{head("Review Application")}
<style>a{{text-decoration:none}}.review-section{{background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:20px}}.review-section h3{{font-size:16px;font-family:var(--font-body);margin-bottom:16px}}.checklist-item{{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("applications.html")}
<main class="page-content" style="max-width:800px">
  <a href="applications.html" style="font-size:13px;color:var(--gm-earth-500);display:block;margin-bottom:16px">← Back to Applications</a>
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:32px"><div><h1 class="page-title">Eco Bloom Gardens</h1><p class="page-subtitle">Agriculture • Nairobi, Kenya • Submitted Mar 16, 2026</p></div><span class="badge badge-amber" style="font-size:13px;padding:6px 14px">Pending Review</span></div>
  <div class="review-section"><h3>Enterprise Information</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;font-size:14px"><div><strong style="color:var(--gm-earth-500);font-size:12px;display:block;margin-bottom:2px">Type</strong>Social Enterprise</div><div><strong style="color:var(--gm-earth-500);font-size:12px;display:block;margin-bottom:2px">Sector</strong>Agriculture, Food & Beverages</div><div><strong style="color:var(--gm-earth-500);font-size:12px;display:block;margin-bottom:2px">Location</strong>Nairobi, Kenya</div><div><strong style="color:var(--gm-earth-500);font-size:12px;display:block;margin-bottom:2px">Website</strong>ecobloomgardens.co.ke</div></div><div style="margin-top:16px"><strong style="color:var(--gm-earth-500);font-size:12px;display:block;margin-bottom:4px">Description</strong><p style="font-size:14px;color:var(--gm-earth-600);line-height:1.7">Eco Bloom Gardens is an urban farming initiative in Nairobi that grows organic vegetables using vertical farming techniques. We supply fresh produce to local markets and restaurants while training youth in sustainable agriculture.</p></div></div>
  <div class="review-section"><h3>Curation Checklist</h3><div class="checklist-item"><input type="checkbox"> Meets minimum sector standards</div><div class="checklist-item"><input type="checkbox"> Good for people (social impact verified)</div><div class="checklist-item"><input type="checkbox"> Good for the planet (environmental practices)</div><div class="checklist-item"><input type="checkbox"> Transparent business practices</div><div class="checklist-item"><input type="checkbox"> Contact information verified</div></div>
  <div class="review-section"><h3>Reviewer Notes</h3><textarea class="form-textarea" rows="4" placeholder="Add notes about this application..."></textarea></div>
  <div style="display:flex;gap:12px;justify-content:flex-end"><button class="btn btn-secondary">Request More Info</button><button class="btn" style="background:var(--gm-amber-500);color:var(--gm-earth-900);border-color:var(--gm-amber-500)">Needs Improvement</button><button class="btn btn-primary">Approve ✓</button></div>
</main></div>{foot()}'''

pages["admin/enterprises.html"] = f'''{head("Manage Enterprises")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("enterprises.html")}
<main class="page-content"><h1 class="page-title">Enterprises</h1><p class="page-subtitle" style="margin-bottom:32px">Manage all Good Market approved enterprises</p>
  <div style="display:flex;gap:12px;margin-bottom:24px"><div style="flex:1;display:flex;background:var(--gm-earth-100);border-radius:var(--radius-md);padding:8px 14px;gap:8px;align-items:center"><span>🔍</span><input style="border:none;background:none;flex:1;outline:none;font-size:14px" placeholder="Search enterprises..."></div><select class="form-select" style="padding:8px 14px;font-size:13px"><option>All Levels</option><option>Level 5</option><option>Level 4</option><option>Level 3</option><option>Level 2</option><option>Level 1</option></select><select class="form-select" style="padding:8px 14px;font-size:13px"><option>All Sectors</option><option>Food</option><option>Fashion</option><option>Tech</option></select></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);overflow:hidden"><table class="data-table"><thead><tr><th>Enterprise</th><th>Sector</th><th>Country</th><th>Level</th><th>Status</th><th>Members</th><th>Actions</th></tr></thead><tbody>
    <tr><td><strong>Green Harvest Organics</strong></td><td>Food</td><td>Sri Lanka</td><td><span class="badge badge-amber">Level 4</span></td><td><span class="badge badge-green">Active</span></td><td>312</td><td><a href="../public/enterprise-profile.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    <tr><td><strong>Artisan Collective</strong></td><td>Crafts</td><td>Kenya</td><td><span class="badge badge-green">Level 5</span></td><td><span class="badge badge-green">Active</span></td><td>256</td><td><a href="../public/enterprise-profile.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    <tr><td><strong>Zero Waste Co.</strong></td><td>Packaging</td><td>Netherlands</td><td><span class="badge badge-earth">Level 3</span></td><td><span class="badge badge-green">Active</span></td><td>189</td><td><a href="../public/enterprise-profile.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    <tr><td><strong>Nature's Touch</strong></td><td>Wellness</td><td>India</td><td><span class="badge badge-amber">Level 4</span></td><td><span class="badge badge-green">Active</span></td><td>145</td><td><a href="../public/enterprise-profile.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    <tr><td><strong>Sunset Farms</strong></td><td>Agriculture</td><td>Australia</td><td><span class="badge badge-earth">Level 2</span></td><td><span class="badge badge-amber">Under Review</span></td><td>67</td><td><a href="../public/enterprise-profile.html" class="btn btn-sm btn-ghost">View</a></td></tr>
  </tbody></table></div>
</main></div>{foot()}'''

pages["admin/users.html"] = f'''{head("Manage Users")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("users.html")}
<main class="page-content"><h1 class="page-title">Users</h1><p class="page-subtitle" style="margin-bottom:32px">Manage platform user accounts</p>
  <div style="display:flex;gap:12px;margin-bottom:24px"><div style="flex:1;display:flex;background:var(--gm-earth-100);border-radius:var(--radius-md);padding:8px 14px;gap:8px;align-items:center"><span>🔍</span><input style="border:none;background:none;flex:1;outline:none;font-size:14px" placeholder="Search users..."></div><select class="form-select" style="padding:8px 14px;font-size:13px"><option>All Roles</option><option>Personal</option><option>Enterprise</option><option>Admin</option></select></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);overflow:hidden"><table class="data-table"><thead><tr><th>User</th><th>Email</th><th>Role</th><th>Joined</th><th>Last Active</th><th>Actions</th></tr></thead><tbody>
    <tr><td><div style="display:flex;align-items:center;gap:8px"><div style="width:28px;height:28px;border-radius:50%;background:var(--gm-green-200);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:var(--gm-green-800)">JD</div>John Doe</div></td><td>john@example.com</td><td><span class="badge badge-sky">Personal</span></td><td>Jan 2024</td><td>Today</td><td><button class="btn btn-sm btn-ghost">Edit</button></td></tr>
    <tr><td><div style="display:flex;align-items:center;gap:8px"><div style="width:28px;height:28px;border-radius:50%;background:var(--gm-amber-100);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:var(--gm-amber-600)">SK</div>Saman Kumara</div></td><td>saman@greenharv.lk</td><td><span class="badge badge-green">Enterprise</span></td><td>Mar 2018</td><td>Yesterday</td><td><button class="btn btn-sm btn-ghost">Edit</button></td></tr>
    <tr><td><div style="display:flex;align-items:center;gap:8px"><div style="width:28px;height:28px;border-radius:50%;background:var(--gm-coral-100);display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:var(--gm-coral-600)">AD</div>Admin Demo</div></td><td>admin@goodmarket.global</td><td><span class="badge badge-coral">Admin</span></td><td>Feb 2016</td><td>Today</td><td><button class="btn btn-sm btn-ghost">Edit</button></td></tr>
  </tbody></table></div>
</main></div>{foot()}'''

pages["admin/reports.html"] = f'''{head("Reports")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("reports.html")}
<main class="page-content"><h1 class="page-title">Platform Reports</h1><p class="page-subtitle" style="margin-bottom:32px">Analytics and insights across the Good Market platform</p>
  <div style="display:flex;gap:12px;margin-bottom:32px"><select class="form-select" style="padding:8px 16px;font-size:13px"><option>Last 30 days</option><option>Last 90 days</option><option>This year</option><option>All time</option></select><button class="btn btn-sm btn-secondary">↓ Export CSV</button></div>
  <div class="grid grid-4 gap-4" style="margin-bottom:32px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500)">New Enterprises</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">148</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500)">Marketplace Revenue</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">$128K</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500)">Active Users</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">8,420</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:20px"><div style="font-size:12px;color:var(--gm-earth-500)">Countries Active</div><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">94</div></div>
  </div>
  <div class="grid grid-2 gap-6">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Growth Over Time</h3><div style="background:var(--gm-earth-50);border:2px dashed var(--gm-earth-200);border-radius:var(--radius-lg);height:280px;display:flex;align-items:center;justify-content:center;color:var(--gm-earth-400)">📊 Platform growth chart</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Top Sectors</h3><div style="background:var(--gm-earth-50);border:2px dashed var(--gm-earth-200);border-radius:var(--radius-lg);height:280px;display:flex;align-items:center;justify-content:center;color:var(--gm-earth-400)">📊 Sector distribution chart</div></div>
  </div>
</main></div>{foot()}'''

pages["admin/curation.html"] = f'''{head("Curation")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("curation.html")}
<main class="page-content"><h1 class="page-title">Curation Tools</h1><p class="page-subtitle" style="margin-bottom:32px">Manage curation standards and review processes</p>
  <div class="grid grid-3 gap-6" style="margin-bottom:32px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:12px">📋 Sector Standards</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:16px">Define and manage minimum standards for each sector</p><a href="#" class="btn btn-sm btn-secondary">Manage Standards</a></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:12px">⭐ Level Assessment</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:16px">Review and adjust enterprise Good Market levels</p><a href="#" class="btn btn-sm btn-secondary">Assess Levels</a></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:12px">🚩 Flagged Items</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:16px">Review flagged enterprises, listings, and feedback</p><a href="#" class="btn btn-sm btn-primary">12 pending reviews</a></div>
  </div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Recent Curation Activity</h3>
    <div style="display:flex;flex-direction:column;gap:12px">
      <div style="display:flex;justify-content:space-between;align-items:center;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div><strong style="font-size:13px">Eco Bloom Gardens</strong> — Application reviewed</div><span style="font-size:12px;color:var(--gm-earth-500)">2 hours ago</span></div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div><strong style="font-size:13px">Green Harvest Organics</strong> — Level upgraded to 4</div><span style="font-size:12px;color:var(--gm-earth-500)">1 day ago</span></div>
      <div style="display:flex;justify-content:space-between;align-items:center;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div><strong style="font-size:13px">Urban Fashion Co.</strong> — Listing flagged for review</div><span style="font-size:12px;color:var(--gm-earth-500)">2 days ago</span></div>
    </div>
  </div>
</main></div>{foot()}'''

pages["admin/settings.html"] = f'''{head("Admin Settings")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("settings.html")}
<main class="page-content"><h1 class="page-title">Platform Settings</h1><p class="page-subtitle" style="margin-bottom:32px">Configure global platform settings</p>
  <div style="max-width:720px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">General</h3>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Platform Name</label><input class="form-input" value="Good Market"></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Default Currency</label><select class="form-select" style="width:100%"><option>USD</option><option>EUR</option><option>GBP</option><option>LKR</option></select></div>
      <div class="form-group"><label class="form-label">Default Language</label><select class="form-select" style="width:100%"><option>English</option><option>Sinhala</option><option>Tamil</option><option>Spanish</option></select></div>
    </div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Marketplace</h3>
      <label style="display:flex;align-items:center;gap:10px;padding:12px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px"><input type="checkbox" checked> Enable cart checkout</label>
      <label style="display:flex;align-items:center;gap:10px;padding:12px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px"><input type="checkbox" checked> Show price currency conversion</label>
      <label style="display:flex;align-items:center;gap:10px;padding:12px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px"><input type="checkbox" checked> Enable community feedback</label>
      <label style="display:flex;align-items:center;gap:10px;padding:12px 0;font-size:14px"><input type="checkbox"> Enable forum</label>
    </div>
    <div style="display:flex;gap:12px;justify-content:flex-end"><button class="btn btn-primary">Save Settings</button></div>
  </div>
</main></div>{foot()}'''

# ========== REMAINING PUBLIC PAGES ==========
pages["public/categories.html"] = f'''{head("Categories","../","marketplace")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#146B43);padding:60px 0;color:#fff;text-align:center"><h1 style="font-size:36px;margin-bottom:8px">Browse Categories</h1><p style="opacity:.85;font-size:16px">Explore products and services by category</p></div>
<div class="container" style="padding:40px 24px 60px"><div class="grid grid-4 gap-6">
  <a href="marketplace.html?cat=food" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">🍎</div><h3 style="font-size:18px;margin-bottom:4px">Food & Beverages</h3><p style="font-size:13px;color:var(--gm-earth-500)">842 listings</p></a>
  <a href="marketplace.html?cat=fashion" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">👗</div><h3 style="font-size:18px;margin-bottom:4px">Fashion & Textiles</h3><p style="font-size:13px;color:var(--gm-earth-500)">531 listings</p></a>
  <a href="marketplace.html?cat=wellness" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">💆</div><h3 style="font-size:18px;margin-bottom:4px">Health & Wellness</h3><p style="font-size:13px;color:var(--gm-earth-500)">327 listings</p></a>
  <a href="marketplace.html?cat=crafts" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">🎨</div><h3 style="font-size:18px;margin-bottom:4px">Arts & Crafts</h3><p style="font-size:13px;color:var(--gm-earth-500)">245 listings</p></a>
  <a href="marketplace.html?cat=home" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">🏡</div><h3 style="font-size:18px;margin-bottom:4px">Home & Garden</h3><p style="font-size:13px;color:var(--gm-earth-500)">289 listings</p></a>
  <a href="marketplace.html?cat=tech" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">💡</div><h3 style="font-size:18px;margin-bottom:4px">Technology</h3><p style="font-size:13px;color:var(--gm-earth-500)">156 listings</p></a>
  <a href="marketplace.html?cat=services" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">🔧</div><h3 style="font-size:18px;margin-bottom:4px">Services</h3><p style="font-size:13px;color:var(--gm-earth-500)">412 listings</p></a>
  <a href="marketplace.html?cat=travel" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center;text-decoration:none;color:inherit;transition:all .25s;display:block"><div style="font-size:48px;margin-bottom:12px">🏕</div><h3 style="font-size:18px;margin-bottom:4px">Travel & Experiences</h3><p style="font-size:13px;color:var(--gm-earth-500)">198 listings</p></a>
</div></div>{foot()}'''

pages["public/about.html"] = f'''{head("About","../","about")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#20A96A);padding:80px 0;color:#fff;text-align:center"><h1 style="font-size:42px;margin-bottom:12px">About Good Market</h1><p style="opacity:.85;font-size:18px;max-width:600px;margin:0 auto">A digital commons for the new economy movement</p></div>
<div class="container" style="padding:60px 24px">
  <div style="max-width:800px;margin:0 auto">
    <div style="background:#fff;border-radius:var(--radius-xl);padding:40px;margin-bottom:32px;border:1px solid var(--gm-earth-200)"><h2 style="font-size:24px;margin-bottom:16px">Our Mission</h2><p style="font-size:15px;line-height:1.8;color:var(--gm-earth-600)">Good Market is a curated community platform and digital commons for the new economy movement. We make it easier to find and connect with social enterprises, cooperatives, responsible businesses, civic organizations, networks, and changemakers who are creating a better world. The goal is to catalyze the transition to a new economy by increasing the visibility of the movement and facilitating trade, collaboration, and collective action.</p></div>
    <div class="grid grid-3 gap-6" style="margin-bottom:32px">
      <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-align:center"><div style="font-size:36px;margin-bottom:12px">🌱</div><h3 style="font-size:16px;margin-bottom:8px">Support Transparency</h3><p style="font-size:13px;color:var(--gm-earth-500);line-height:1.6">Sharing information improves learning, builds trust, and speeds the rate of change.</p></div>
      <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-align:center"><div style="font-size:36px;margin-bottom:12px">🤝</div><h3 style="font-size:16px;margin-bottom:8px">Think Ecosystem</h3><p style="font-size:13px;color:var(--gm-earth-500);line-height:1.6">Enterprises differentiate to fill gaps and create value, not compete with one another.</p></div>
      <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-align:center"><div style="font-size:36px;margin-bottom:12px">♻️</div><h3 style="font-size:16px;margin-bottom:8px">Continuous Improvement</h3><p style="font-size:13px;color:var(--gm-earth-500);line-height:1.6">Instead of waiting for perfection, we focus on minimum standards and continuous improvement.</p></div>
    </div>
    <div style="background:#fff;border-radius:var(--radius-xl);padding:40px;border:1px solid var(--gm-earth-200)"><h2 style="font-size:24px;margin-bottom:16px">Our Story</h2><p style="font-size:15px;line-height:1.8;color:var(--gm-earth-600);margin-bottom:16px">Good Market began in Sri Lanka in 2012 with no grant funding or external working capital. The curation process and community were initially developed through weekly marketplace events, retail outlets, and an organic participatory guarantee system (PGS). These social enterprises made it possible to start software development for the global digital commons in 2016.</p><p style="font-size:15px;line-height:1.8;color:var(--gm-earth-600)">Good Market operates as a not-for-profit, self-sustaining social enterprise. It generates revenue, but does not have private shareholders. It exists to benefit the community. Any surplus is reinvested to improve and expand services.</p></div>
  </div>
</div>{foot()}'''

pages["public/impact.html"] = f'''{head("Impact","../","impact")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#20A96A);padding:80px 0;color:#fff;text-align:center"><h1 style="font-size:42px;margin-bottom:12px">Our Impact</h1><p style="opacity:.85;font-size:18px;max-width:560px;margin:0 auto">Measuring the movement toward a better economy</p></div>
<div class="container" style="padding:60px 24px">
  <div class="grid grid-4 gap-6" style="margin-bottom:48px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center"><div style="font-family:var(--font-display);font-size:42px;color:var(--gm-green-600)">4,832</div><div style="font-size:14px;color:var(--gm-earth-500);margin-top:4px">Approved Enterprises</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center"><div style="font-family:var(--font-display);font-size:42px;color:var(--gm-green-600)">94</div><div style="font-size:14px;color:var(--gm-earth-500);margin-top:4px">Countries Represented</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center"><div style="font-family:var(--font-display);font-size:42px;color:var(--gm-green-600)">$2.4M</div><div style="font-size:14px;color:var(--gm-earth-500);margin-top:4px">Community Trade Volume</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px;text-align:center"><div style="font-family:var(--font-display);font-size:42px;color:var(--gm-green-600)">52</div><div style="font-size:14px;color:var(--gm-earth-500);margin-top:4px">Active Networks</div></div>
  </div>
  <div class="grid grid-2 gap-8">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px"><h3 style="font-size:20px;margin-bottom:16px">🌍 Global Reach</h3><div style="background:var(--gm-earth-50);border:2px dashed var(--gm-earth-200);border-radius:var(--radius-lg);height:300px;display:flex;align-items:center;justify-content:center;color:var(--gm-earth-400)">🗺 Interactive world map of enterprises</div></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:32px"><h3 style="font-size:20px;margin-bottom:16px">📈 Growth Over Time</h3><div style="background:var(--gm-earth-50);border:2px dashed var(--gm-earth-200);border-radius:var(--radius-lg);height:300px;display:flex;align-items:center;justify-content:center;color:var(--gm-earth-400)">📊 Enterprise growth timeline chart</div></div>
  </div>
</div>{foot()}'''

pages["public/events.html"] = f'''{head("Events","../","events")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#146B43);padding:60px 0;color:#fff;text-align:center"><h1 style="font-size:36px;margin-bottom:8px">Events</h1><p style="opacity:.85;font-size:16px">Marketplace events, workshops, and community gatherings</p></div>
<div class="container" style="padding:40px 24px 60px">
  <div class="tabs" style="margin-bottom:32px"><a class="tab active">Upcoming</a><a class="tab">Past Events</a><a class="tab">My Events</a></div>
  <div class="grid grid-3 gap-6">
    <div class="card"><img class="card-img" src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=400&h=300&fit=crop" alt="Market"><div class="card-body"><span class="badge badge-green" style="margin-bottom:8px">In Person</span><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Saturday Good Market</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:8px">📍 Racecourse Grounds, Colombo<br>📅 Every Saturday, 8AM – 2PM</p><a href="#" class="btn btn-sm btn-primary" style="width:100%">Learn More</a></div></div>
    <div class="card"><img class="card-img" src="https://images.unsplash.com/photo-1515187029135-18ee286d815b?w=400&h=300&fit=crop" alt="Workshop"><div class="card-body"><span class="badge badge-sky" style="margin-bottom:8px">Online</span><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Sustainable Packaging Workshop</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:8px">📍 Zoom<br>📅 Mar 25, 2026, 3PM UTC</p><a href="#" class="btn btn-sm btn-primary" style="width:100%">Register</a></div></div>
    <div class="card"><img class="card-img" src="https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?w=400&h=300&fit=crop" alt="Festival"><div class="card-body"><span class="badge badge-amber" style="margin-bottom:8px">Festival</span><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Good Market Earth Day Festival</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:8px">📍 Viharamahadevi Park, Colombo<br>📅 Apr 22, 2026</p><a href="#" class="btn btn-sm btn-primary" style="width:100%">Get Tickets</a></div></div>
  </div>
</div>{foot()}'''

pages["public/blog.html"] = f'''{head("Blog","../","about")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#146B43);padding:60px 0;color:#fff;text-align:center"><h1 style="font-size:36px;margin-bottom:8px">Blog</h1><p style="opacity:.85;font-size:16px">Stories, insights, and news from the Good Market community</p></div>
<div class="container" style="padding:40px 24px 60px;max-width:900px">
  <div class="grid gap-8" style="grid-template-columns:1fr">
    <article style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);overflow:hidden;display:grid;grid-template-columns:300px 1fr"><img src="https://images.unsplash.com/photo-1542838132-92c53300491e?w=400&h=300&fit=crop" style="width:100%;height:100%;object-fit:cover" alt=""><div style="padding:28px"><span class="badge badge-green" style="margin-bottom:8px">Community</span><h2 style="font-size:20px;margin-bottom:8px"><a href="#" style="color:inherit;text-decoration:none">How Organic PGS is Transforming Sri Lankan Agriculture</a></h2><p style="font-size:14px;color:var(--gm-earth-500);line-height:1.7;margin-bottom:12px">The participatory guarantee system has empowered over 45 farms across 12 districts to transition to organic farming methods...</p><div style="display:flex;align-items:center;gap:8px;font-size:12px;color:var(--gm-earth-400)"><span>Mar 12, 2026</span><span>•</span><span>5 min read</span></div></div></article>
    <article style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);overflow:hidden;display:grid;grid-template-columns:300px 1fr"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=400&h=300&fit=crop" style="width:100%;height:100%;object-fit:cover" alt=""><div style="padding:28px"><span class="badge badge-amber" style="margin-bottom:8px">Fashion</span><h2 style="font-size:20px;margin-bottom:8px"><a href="#" style="color:inherit;text-decoration:none">The Rise of Ethical Fashion in East Africa</a></h2><p style="font-size:14px;color:var(--gm-earth-500);line-height:1.7;margin-bottom:12px">Meet the artisans and designers building a sustainable fashion industry across Kenya, Uganda, and Tanzania...</p><div style="display:flex;align-items:center;gap:8px;font-size:12px;color:var(--gm-earth-400)"><span>Mar 8, 2026</span><span>•</span><span>7 min read</span></div></div></article>
    <article style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);overflow:hidden;display:grid;grid-template-columns:300px 1fr"><img src="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?w=400&h=300&fit=crop" style="width:100%;height:100%;object-fit:cover" alt=""><div style="padding:28px"><span class="badge badge-sky" style="margin-bottom:8px">Technology</span><h2 style="font-size:20px;margin-bottom:8px"><a href="#" style="color:inherit;text-decoration:none">Zero Waste Packaging: Innovation in the Netherlands</a></h2><p style="font-size:14px;color:var(--gm-earth-500);line-height:1.7;margin-bottom:12px">Dutch social enterprises are pioneering compostable and reusable packaging solutions for the food industry...</p><div style="display:flex;align-items:center;gap:8px;font-size:12px;color:var(--gm-earth-400)"><span>Mar 3, 2026</span><span>•</span><span>4 min read</span></div></div></article>
  </div>
</div>{foot()}'''

pages["public/standards.html"] = f'''{head("The Rules","../","about")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#146B43);padding:60px 0;color:#fff;text-align:center"><h1 style="font-size:36px;margin-bottom:8px">The Rules</h1><p style="opacity:.85;font-size:16px">Curation process and minimum standards</p></div>
<div class="container" style="padding:40px 24px 60px;max-width:800px">
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:36px;margin-bottom:24px"><h2 style="font-size:22px;margin-bottom:16px">Curation Process</h2><p style="font-size:14px;line-height:1.8;color:var(--gm-earth-600)">Good Market uses a community-owned curation process and crowdsourced monitoring system. Applicants are never "rejected" — they are encouraged to make improvements and reapply. The process works across economic sectors, income levels, language barriers, and regional divides.</p></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:36px;margin-bottom:24px"><h2 style="font-size:22px;margin-bottom:16px">Good Market Levels</h2><div style="display:flex;flex-direction:column;gap:12px"><div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div style="display:flex;gap:3px"><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div></div><div><strong style="font-size:14px">Level 1</strong><p style="font-size:12px;color:var(--gm-earth-500)">Meets minimum standards</p></div></div><div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div style="display:flex;gap:3px"><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div></div><div><strong style="font-size:14px">Level 2</strong><p style="font-size:12px;color:var(--gm-earth-500)">Above minimum standards</p></div></div><div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div style="display:flex;gap:3px"><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div></div><div><strong style="font-size:14px">Level 3</strong><p style="font-size:12px;color:var(--gm-earth-500)">Strong social/environmental commitment</p></div></div><div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--gm-earth-50);border-radius:var(--radius-md)"><div style="display:flex;gap:3px"><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div></div><div><strong style="font-size:14px">Level 4</strong><p style="font-size:12px;color:var(--gm-earth-500)">Strong focus on impact</p></div></div><div style="display:flex;align-items:center;gap:12px;padding:12px;background:var(--gm-green-50);border-radius:var(--radius-md)"><div style="display:flex;gap:3px"><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div><div style="width:10px;height:10px;border-radius:50%;background:var(--gm-green-500)"></div></div><div><strong style="font-size:14px">Level 5</strong><p style="font-size:12px;color:var(--gm-earth-500)">Exceptional impact leader</p></div></div></div></div>
</div>{foot()}'''

# Simple template pages
for pg_name, pg_title, pg_icon, pg_desc in [
    ("help.html", "Help Center", "❓", "Find answers to common questions about the Good Market platform"),
    ("contact.html", "Contact", "📧", "Get in touch with the Good Market team"),
    ("donate.html", "Support Us", "💚", "Help sustain the Good Market digital commons"),
    ("volunteer.html", "Volunteer", "🙋", "Contribute your skills and time to the movement"),
    ("translate.html", "Help Translate", "🌐", "Help make Good Market accessible in more languages"),
    ("privacy.html", "Privacy Policy", "🔒", "How Good Market handles your personal information"),
    ("terms.html", "Terms of Service", "📜", "Terms and conditions for using the Good Market platform"),
    ("accessibility.html", "Accessibility", "♿", "Our commitment to making Good Market accessible to everyone"),
    ("forum.html", "Community Forum", "💬", "Ask questions and share knowledge with the community"),
    ("search-results.html", "Search Results", "🔍", "Showing results for your search query"),
]:
    content = f"<p style='font-size:14px;line-height:1.8;color:var(--gm-earth-600)'>{pg_desc}. This is a demonstration page for the Good Market redesign prototype. In the live version, this page would contain full content and interactive features.</p>"
    if pg_name == "contact.html":
        content = f"""<div class="grid grid-2 gap-8"><div><h3 style="font-size:18px;margin-bottom:16px">Send us a message</h3><div class="form-group" style="margin-bottom:16px"><label class="form-label">Name</label><input class="form-input" placeholder="Your name"></div><div class="form-group" style="margin-bottom:16px"><label class="form-label">Email</label><input class="form-input" placeholder="you@example.com"></div><div class="form-group" style="margin-bottom:16px"><label class="form-label">Subject</label><select class="form-select" style="width:100%"><option>General Inquiry</option><option>Application Help</option><option>Technical Support</option><option>Partnership</option></select></div><div class="form-group" style="margin-bottom:16px"><label class="form-label">Message</label><textarea class="form-textarea" rows="5" placeholder="How can we help?"></textarea></div><button class="btn btn-primary">Send Message</button></div><div><h3 style="font-size:18px;margin-bottom:16px">Other ways to reach us</h3><div style="display:flex;flex-direction:column;gap:16px;font-size:14px;color:var(--gm-earth-600)"><div style="padding:16px;background:var(--gm-earth-50);border-radius:var(--radius-md)">📧 hello@goodmarket.global</div><div style="padding:16px;background:var(--gm-earth-50);border-radius:var(--radius-md)">📞 +94 77 020 8642</div><div style="padding:16px;background:var(--gm-earth-50);border-radius:var(--radius-md)">💬 Use the Help Chat on the platform</div><div style="padding:16px;background:var(--gm-earth-50);border-radius:var(--radius-md)">📍 Good Market, Colombo, Sri Lanka</div></div></div></div>"""
    elif pg_name == "help.html":
        content = f"""<div class="grid grid-3 gap-6"><a href="#" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-decoration:none;color:inherit;display:block"><div style="font-size:28px;margin-bottom:12px">🚀</div><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Quick Tour</h3><p style="font-size:13px;color:var(--gm-earth-500)">Get started with Good Market in 5 minutes</p></a><a href="#" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-decoration:none;color:inherit;display:block"><div style="font-size:28px;margin-bottom:12px">👤</div><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Personal Account</h3><p style="font-size:13px;color:var(--gm-earth-500)">Login, preferences, feedback, and following</p></a><a href="#" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-decoration:none;color:inherit;display:block"><div style="font-size:28px;margin-bottom:12px">🏢</div><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Enterprise Account</h3><p style="font-size:13px;color:var(--gm-earth-500)">Profile, listings, payments, and networks</p></a><a href="#" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-decoration:none;color:inherit;display:block"><div style="font-size:28px;margin-bottom:12px">🛒</div><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Marketplace</h3><p style="font-size:13px;color:var(--gm-earth-500)">Browsing, searching, and purchasing</p></a><a href="#" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-decoration:none;color:inherit;display:block"><div style="font-size:28px;margin-bottom:12px">📋</div><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Application</h3><p style="font-size:13px;color:var(--gm-earth-500)">How to apply and get approved</p></a><a href="#" style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:28px;text-decoration:none;color:inherit;display:block"><div style="font-size:28px;margin-bottom:12px">🌐</div><h3 style="font-size:16px;margin-bottom:4px;font-family:var(--font-body)">Networks</h3><p style="font-size:13px;color:var(--gm-earth-500)">Joining and managing networks</p></a></div>"""
    elif pg_name == "donate.html":
        content = f"""<div style="text-align:center;max-width:600px;margin:0 auto"><p style="font-size:16px;line-height:1.8;color:var(--gm-earth-600);margin-bottom:32px">Good Market is a not-for-profit social enterprise. Your support helps us maintain and grow this digital commons for the new economy movement.</p><div class="grid grid-3 gap-4" style="margin-bottom:32px"><div style="background:#fff;border:2px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:24px;cursor:pointer;transition:all .2s"><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">$10</div><div style="font-size:12px;color:var(--gm-earth-500);margin-top:4px">Supporter</div></div><div style="background:var(--gm-green-50);border:2px solid var(--gm-green-500);border-radius:var(--radius-xl);padding:24px;cursor:pointer"><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">$25</div><div style="font-size:12px;color:var(--gm-earth-500);margin-top:4px">Champion</div></div><div style="background:#fff;border:2px solid var(--gm-earth-200);border-radius:var(--radius-xl);padding:24px;cursor:pointer;transition:all .2s"><div style="font-family:var(--font-display);font-size:28px;color:var(--gm-green-600)">$50</div><div style="font-size:12px;color:var(--gm-earth-500);margin-top:4px">Cocreator</div></div></div><button class="btn btn-primary btn-lg" style="width:100%;max-width:300px">Donate Now 💚</button></div>"""
    pages[f"public/{pg_name}"] = f'''{head(pg_title,"../","about")}
<body><div id="gm-nav"></div>
<div style="background:linear-gradient(135deg,#0B3D2E,#146B43);padding:60px 0;color:#fff;text-align:center"><h1 style="font-size:36px;margin-bottom:8px">{pg_icon} {pg_title}</h1><p style="opacity:.85;font-size:16px">{pg_desc}</p></div>
<div class="container" style="padding:40px 24px 60px">{content}</div>{foot()}'''

pages["public/map-view.html"] = f'''{head("Map View","../","directory")}
<body><div id="gm-nav"></div>
<div style="height:calc(100vh - 72px);display:flex;flex-direction:column">
  <div style="padding:12px 24px;background:#fff;border-bottom:1px solid var(--gm-earth-200);display:flex;align-items:center;justify-content:space-between">
    <div style="display:flex;align-items:center;gap:12px"><h2 style="font-size:18px">Map View</h2><span style="font-size:13px;color:var(--gm-earth-500)">4,832 enterprises</span></div>
    <div style="display:flex;gap:8px"><select class="form-select" style="padding:6px 12px;font-size:13px"><option>All Categories</option><option>🍽 Restaurants</option><option>🏨 Hotels</option><option>🛍 Retail</option><option>💆 Wellness</option><option>🌿 Farms</option></select><a href="directory.html" class="btn btn-sm btn-secondary">Grid View</a></div>
  </div>
  <div style="flex:1;background:var(--gm-earth-100);display:flex;align-items:center;justify-content:center;position:relative"><div style="text-align:center;color:var(--gm-earth-400)"><div style="font-size:64px;margin-bottom:12px">🗺</div><p style="font-size:16px">Interactive map will render here</p><p style="font-size:13px;margin-top:4px">Powered by Google Maps — showing cafes, restaurants, hotels, retail outlets, wellness centers, coworking spaces, and organic farms</p></div>
    <div style="position:absolute;top:16px;left:16px;background:#fff;border-radius:var(--radius-lg);padding:16px;box-shadow:var(--shadow-lg);width:300px"><input class="form-input" placeholder="Search location..." style="margin-bottom:12px;width:100%"><div style="font-size:12px;color:var(--gm-earth-500)">📍 Click map pins to see enterprise details</div></div>
  </div>
</div>{foot()}'''

# Remaining seller pages
pages["seller/edit-listing.html"] = f'''{head("Edit Listing")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("listings.html")}
<main class="page-content"><a href="listings.html" style="font-size:13px;color:var(--gm-earth-500);display:block;margin-bottom:16px">← Back to Listings</a><h1 class="page-title">Edit Listing</h1><p class="page-subtitle" style="margin-bottom:32px">Update your marketplace listing</p>
  <div style="max-width:720px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Listing Details</h3>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Title</label><input class="form-input" value="True Ceylon Cinnamon Sticks — 100g"></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><div class="form-group"><label class="form-label">Price (USD)</label><input class="form-input" type="number" value="12.50"></div><div class="form-group"><label class="form-label">Stock</label><input class="form-input" type="number" value="245"></div></div>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Description</label><textarea class="form-textarea" rows="4">Hand-harvested True Ceylon Cinnamon from our organic farm in Ratnapura, Sri Lanka. Delicate, sweet flavour with low coumarin content.</textarea></div>
      <div class="form-group"><label class="form-label">Keywords</label><input class="form-input" value="organic, cinnamon, ceylon, sri lanka, spices, fair trade"></div>
    </div>
    <div style="display:flex;gap:12px;justify-content:flex-end"><button class="btn btn-secondary">Cancel</button><button class="btn btn-primary">Save Changes</button></div>
  </div>
</main></div>{foot()}'''

pages["seller/settings.html"] = f'''{head("Seller Settings")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("settings.html")}
<main class="page-content"><h1 class="page-title">Settings</h1><p class="page-subtitle" style="margin-bottom:32px">Manage your enterprise account settings</p>
  <div style="max-width:600px">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Notifications</h3>
      <label style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px">New orders<input type="checkbox" checked></label>
      <label style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px">New feedback<input type="checkbox" checked></label>
      <label style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--gm-earth-100);font-size:14px">New followers<input type="checkbox" checked></label>
      <label style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;font-size:14px">Platform announcements<input type="checkbox"></label>
    </div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:28px;margin-bottom:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:20px">Payment Settings</h3>
      <div class="form-group" style="margin-bottom:16px"><label class="form-label">Payout Method</label><select class="form-select" style="width:100%"><option>Bank Transfer</option><option>PayPal</option></select></div>
      <div class="form-group"><label class="form-label">Payout Currency</label><select class="form-select" style="width:100%"><option>USD</option><option>LKR</option><option>EUR</option></select></div>
    </div>
    <button class="btn btn-primary">Save Settings</button>
  </div>
</main></div>{foot()}'''

pages["seller/network-manage.html"] = f'''{head("Manage Networks")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("network-manage.html")}
<main class="page-content"><h1 class="page-title">Networks</h1><p class="page-subtitle" style="margin-bottom:32px">Your network memberships and opportunities</p>
  <div class="tabs" style="margin-bottom:24px"><a class="tab active">My Networks (2)</a><a class="tab">Discover Networks</a></div>
  <div class="grid grid-2 gap-6">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><div style="display:flex;align-items:center;gap:12px;margin-bottom:16px"><div style="width:48px;height:48px;border-radius:var(--radius-md);background:var(--gm-green-100);display:flex;align-items:center;justify-content:center;font-size:24px">🌿</div><div><strong style="font-size:15px">Organic PGS Sri Lanka</strong><p style="font-size:12px;color:var(--gm-earth-500)">124 members</p></div></div><p style="font-size:13px;color:var(--gm-earth-600);margin-bottom:16px">Participatory guarantee system for organic farmers across Sri Lanka</p><a href="../public/network-detail.html" class="btn btn-sm btn-secondary">View Network</a></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><div style="display:flex;align-items:center;gap:12px;margin-bottom:16px"><div style="width:48px;height:48px;border-radius:var(--radius-md);background:var(--gm-amber-100);display:flex;align-items:center;justify-content:center;font-size:24px">🏪</div><div><strong style="font-size:15px">Lanka Spice Export Network</strong><p style="font-size:12px;color:var(--gm-earth-500)">56 members</p></div></div><p style="font-size:13px;color:var(--gm-earth-600);margin-bottom:16px">Connecting Sri Lankan spice producers with international buyers</p><a href="../public/network-detail.html" class="btn btn-sm btn-secondary">View Network</a></div>
  </div>
</main></div>{foot()}'''

pages["seller/order-detail.html"] = f'''{head("Order Detail")}
<style>.sell-link{{display:flex;align-items:center;gap:10px;padding:10px 24px;font-size:14px;color:var(--gm-earth-600);text-decoration:none}}.sell-link.active{{background:var(--gm-green-50);color:var(--gm-green-700);font-weight:600;border-left:3px solid var(--gm-green-500)}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{seller_sidebar("orders.html")}
<main class="page-content"><a href="orders.html" style="font-size:13px;color:var(--gm-earth-500);display:block;margin-bottom:16px">← Back to Orders</a>
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:32px"><div><h1 class="page-title">Order #GM-4821</h1><p class="page-subtitle">Placed on March 16, 2026</p></div><span class="badge badge-green" style="font-size:13px;padding:6px 14px">Shipped</span></div>
  <div class="grid grid-2 gap-6">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:16px">Order Items</h3>
      <div style="display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--gm-earth-100)"><img src="https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=80&h=80&fit=crop" style="width:48px;height:48px;border-radius:6px;object-fit:cover" alt=""><div><strong style="font-size:13px">Ceylon Cinnamon Sticks</strong><p style="font-size:12px;color:var(--gm-earth-500)">Qty: 2 × $12.50</p></div><strong style="margin-left:auto;font-size:14px">$25.00</strong></div>
      <div style="display:flex;justify-content:space-between;padding:12px 0;font-weight:600"><span>Total</span><span style="color:var(--gm-green-700)">$25.00</span></div>
    </div>
    <div><div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px;margin-bottom:20px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:12px">Customer</h3><div style="font-size:14px;color:var(--gm-earth-600)"><strong>Jane Doe</strong><p>jane@example.com</p><p style="margin-top:8px">123 Main Street<br>London, UK WC2N 5DU</p></div></div>
      <div style="display:flex;gap:8px"><button class="btn btn-primary btn-sm">Mark as Delivered</button><button class="btn btn-secondary btn-sm">Print Label</button></div>
    </div>
  </div>
</main></div>{foot()}'''

pages["admin/listings-review.html"] = f'''{head("Listings Review")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("listings-review.html")}
<main class="page-content"><h1 class="page-title">Listings Review</h1><p class="page-subtitle" style="margin-bottom:32px">Review and moderate marketplace listings</p>
  <div class="tabs" style="margin-bottom:24px"><a class="tab active">Pending (15)</a><a class="tab">Flagged (3)</a><a class="tab">Approved (8,420)</a></div>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);overflow:hidden"><table class="data-table"><thead><tr><th>Listing</th><th>Enterprise</th><th>Category</th><th>Price</th><th>Status</th><th>Action</th></tr></thead><tbody>
    <tr><td><strong>Whole Cloves — 50g</strong></td><td>Green Harvest Organics</td><td>Food</td><td>$7.25</td><td><span class="badge badge-amber">Pending</span></td><td><div style="display:flex;gap:4px"><button class="btn btn-sm btn-primary">Approve</button><button class="btn btn-sm btn-ghost">Review</button></div></td></tr>
    <tr><td><strong>Handknit Wool Scarf</strong></td><td>Highland Crafts</td><td>Fashion</td><td>$35.00</td><td><span class="badge badge-amber">Pending</span></td><td><div style="display:flex;gap:4px"><button class="btn btn-sm btn-primary">Approve</button><button class="btn btn-sm btn-ghost">Review</button></div></td></tr>
    <tr><td><strong>Yoga Retreat Weekend</strong></td><td>Serenity Wellness</td><td>Service</td><td>$150.00</td><td><span class="badge badge-coral">Flagged</span></td><td><div style="display:flex;gap:4px"><button class="btn btn-sm btn-primary">Approve</button><button class="btn btn-sm btn-ghost">Review</button></div></td></tr>
  </tbody></table></div>
</main></div>{foot()}'''

pages["admin/networks-admin.html"] = f'''{head("Networks Admin")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("networks-admin.html")}
<main class="page-content"><h1 class="page-title">Networks Management</h1><p class="page-subtitle" style="margin-bottom:32px">Oversee and manage all platform networks</p>
  <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);overflow:hidden"><table class="data-table"><thead><tr><th>Network</th><th>Coordinator</th><th>Members</th><th>Sector</th><th>Status</th><th>Action</th></tr></thead><tbody>
    <tr><td><strong>Organic PGS Sri Lanka</strong></td><td>Nimal Kumara</td><td>124</td><td>Agriculture</td><td><span class="badge badge-green">Active</span></td><td><a href="../public/network-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    <tr><td><strong>Ethical Fashion Collective</strong></td><td>Amina Wanjiku</td><td>87</td><td>Fashion</td><td><span class="badge badge-green">Active</span></td><td><a href="../public/network-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
    <tr><td><strong>Green Tech Alliance</strong></td><td>Hans Mueller</td><td>92</td><td>Technology</td><td><span class="badge badge-green">Active</span></td><td><a href="../public/network-detail.html" class="btn btn-sm btn-ghost">View</a></td></tr>
  </tbody></table></div>
</main></div>{foot()}'''

pages["admin/content.html"] = f'''{head("Content Management")}
<style>a{{text-decoration:none}}</style>
<body><div id="gm-nav"></div><div style="display:flex">{admin_sidebar("content.html")}
<main class="page-content"><h1 class="page-title">Content Management</h1><p class="page-subtitle" style="margin-bottom:32px">Manage platform content, pages, and announcements</p>
  <div class="grid grid-3 gap-6">
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:8px">📝 Blog Posts</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:16px">12 published, 3 drafts</p><button class="btn btn-sm btn-secondary">Manage Posts</button></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:8px">📢 Announcements</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:16px">Send platform-wide notices</p><button class="btn btn-sm btn-primary">New Announcement</button></div>
    <div style="background:#fff;border:1px solid var(--gm-earth-200);border-radius:var(--radius-lg);padding:24px"><h3 style="font-size:16px;font-family:var(--font-body);margin-bottom:8px">📄 Static Pages</h3><p style="font-size:13px;color:var(--gm-earth-500);margin-bottom:16px">About, Terms, Privacy, Help</p><button class="btn btn-sm btn-secondary">Edit Pages</button></div>
  </div>
</main></div>{foot()}'''

# ========== ROOT INDEX ==========
pages["index.html"] = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Good Market — UI Prototype</title><link rel="stylesheet" href="assets/css/design-system.css">
<style>.idx-hero{{background:linear-gradient(135deg,#0B3D2E,#20A96A);min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff}}.idx-section{{margin-top:40px}}.idx-section h3{{font-size:14px;text-transform:uppercase;letter-spacing:.06em;opacity:.6;margin-bottom:16px}}.idx-links{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}}.idx-link{{padding:10px 20px;background:rgba(255,255,255,.12);border-radius:10px;color:#fff;text-decoration:none;font-size:14px;font-weight:500;transition:all .2s;backdrop-filter:blur(4px)}}.idx-link:hover{{background:rgba(255,255,255,.25);color:#fff;transform:translateY(-2px)}}</style></head><body>
<div class="idx-hero"><div style="max-width:900px;padding:40px">
  <div style="font-size:48px;margin-bottom:16px">🌍</div>
  <h1 style="font-size:48px;margin-bottom:12px">Good Market</h1>
  <p style="font-size:20px;opacity:.85;margin-bottom:8px">Modernised UI/UX Prototype</p>
  <p style="font-size:14px;opacity:.6;margin-bottom:40px">Non-functional demo — 50+ interconnected pages</p>
  <div class="idx-section"><h3>🏠 Public Pages</h3><div class="idx-links">
    <a href="public/home.html" class="idx-link">Home</a><a href="public/marketplace.html" class="idx-link">Marketplace</a><a href="public/product-detail.html" class="idx-link">Product Detail</a><a href="public/directory.html" class="idx-link">Directory</a><a href="public/enterprise-profile.html" class="idx-link">Enterprise Profile</a><a href="public/networks.html" class="idx-link">Networks</a><a href="public/network-detail.html" class="idx-link">Network Detail</a><a href="public/categories.html" class="idx-link">Categories</a><a href="public/map-view.html" class="idx-link">Map View</a><a href="public/impact.html" class="idx-link">Impact</a><a href="public/events.html" class="idx-link">Events</a><a href="public/blog.html" class="idx-link">Blog</a><a href="public/about.html" class="idx-link">About</a><a href="public/standards.html" class="idx-link">The Rules</a><a href="public/help.html" class="idx-link">Help Center</a><a href="public/contact.html" class="idx-link">Contact</a><a href="public/donate.html" class="idx-link">Donate</a><a href="public/forum.html" class="idx-link">Forum</a><a href="public/privacy.html" class="idx-link">Privacy</a><a href="public/terms.html" class="idx-link">Terms</a>
  </div></div>
  <div class="idx-section"><h3>🔐 Auth Pages</h3><div class="idx-links">
    <a href="auth/login.html" class="idx-link">Login</a><a href="auth/register.html" class="idx-link">Register</a><a href="auth/forgot-password.html" class="idx-link">Forgot Password</a><a href="auth/verify-email.html" class="idx-link">Verify Email</a>
  </div></div>
  <div class="idx-section"><h3>🛒 Buyer Pages</h3><div class="idx-links">
    <a href="buyer/dashboard.html" class="idx-link">Dashboard</a><a href="buyer/favorites.html" class="idx-link">Favorites</a><a href="buyer/cart.html" class="idx-link">Cart</a><a href="buyer/checkout.html" class="idx-link">Checkout</a><a href="buyer/order-confirmation.html" class="idx-link">Order Confirmation</a><a href="buyer/orders.html" class="idx-link">Orders</a><a href="buyer/order-detail.html" class="idx-link">Order Detail</a><a href="buyer/messages.html" class="idx-link">Messages</a><a href="buyer/following.html" class="idx-link">Following</a><a href="buyer/reviews.html" class="idx-link">Reviews</a><a href="buyer/settings.html" class="idx-link">Settings</a>
  </div></div>
  <div class="idx-section"><h3>🏪 Seller Pages</h3><div class="idx-links">
    <a href="seller/dashboard.html" class="idx-link">Dashboard</a><a href="seller/listings.html" class="idx-link">My Listings</a><a href="seller/add-listing.html" class="idx-link">Add Listing</a><a href="seller/edit-listing.html" class="idx-link">Edit Listing</a><a href="seller/orders.html" class="idx-link">Orders</a><a href="seller/order-detail.html" class="idx-link">Order Detail</a><a href="seller/analytics.html" class="idx-link">Analytics</a><a href="seller/profile-edit.html" class="idx-link">Edit Profile</a><a href="seller/feedback.html" class="idx-link">Feedback</a><a href="seller/network-manage.html" class="idx-link">Networks</a><a href="seller/subscription.html" class="idx-link">Subscription</a><a href="seller/apply.html" class="idx-link">Apply</a><a href="seller/settings.html" class="idx-link">Settings</a>
  </div></div>
  <div class="idx-section"><h3>⚙️ Admin Pages</h3><div class="idx-links">
    <a href="admin/dashboard.html" class="idx-link">Dashboard</a><a href="admin/applications.html" class="idx-link">Applications</a><a href="admin/application-review.html" class="idx-link">Review App</a><a href="admin/enterprises.html" class="idx-link">Enterprises</a><a href="admin/users.html" class="idx-link">Users</a><a href="admin/listings-review.html" class="idx-link">Listings</a><a href="admin/reports.html" class="idx-link">Reports</a><a href="admin/curation.html" class="idx-link">Curation</a><a href="admin/networks-admin.html" class="idx-link">Networks</a><a href="admin/content.html" class="idx-link">Content</a><a href="admin/settings.html" class="idx-link">Settings</a>
  </div></div>
  <div style="margin-top:48px;opacity:.4;font-size:12px">Built for Good Market modernization demo • March 2026</div>
</div></div></body></html>'''

# ========== WRITE ALL FILES ==========
for filepath, content in pages.items():
    full_path = os.path.join(BASE, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {filepath}")

print(f"\n🎉 Generated {len(pages)} pages!")
