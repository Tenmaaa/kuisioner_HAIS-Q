# ============================
# 🧹 Bersihkan kredensial Git lama
# ============================
Write-Host "Membersihkan kredensial Git lama..."
git config --global --unset credential.helper
git credential-manager-core erase https://github.com

# Hapus semua remote lama
Write-Host "Menghapus remote origin lama (jika ada)..."
try { git remote remove origin } catch {}

# ============================
# 🔧 Konfigurasi user GitHub baru
# ============================
Write-Host "Mengatur konfigurasi Git untuk akun Tenmaaa..."
git config --global user.name "Tenmaaa"
git config --global user.email "email_githubmu@example.com"   # GANTI dengan email GitHub kamu

# ============================
# 🌐 Tambahkan remote baru
# ============================
Write-Host "Menambahkan remote baru untuk akun Tenmaaa..."
git remote add origin https://github.com/Tenmaaa/kuisioner_HAIS-Q.git

# ============================
# 📦 Commit dan push
# ============================
Write-Host "Menambahkan semua file dan membuat commit..."
git add .
git commit -m "Push project dari akun Tenmaaa" --allow-empty

Write-Host "Melakukan push ke GitHub (Tenmaaa)..."
git push -u origin main --force

Write-Host "`n✅ Selesai! Project berhasil diupload ke akun GitHub Tenmaaa."
Write-Host "Jika diminta login, gunakan username: Tenmaaa"
Write-Host "Untuk password, masukkan Personal Access Token (PAT) dari https://github.com/settings/tokens"
