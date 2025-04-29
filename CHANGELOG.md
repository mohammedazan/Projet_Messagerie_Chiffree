# سجل التغييرات - Changelog

## [غير منشور] - 2024-04-21

### ✨ الميزات الجديدة - Features
- إضافة نظام إدارة المفاتيح (`key_manager.py`)
  - توليد مفاتيح AES-256 بشكل آمن
  - تخزين المفاتيح في ملف `secret.key`
  - دعم الرسائل باللغتين العربية والفرنسية
  - نظام اختبارات متكامل

### 🔧 التحسينات التقنية - Technical Improvements
- استخدام مكتبة `cryptography` للتشفير
- تنفيذ نظام التحقق من صحة المفاتيح
- معالجة الأخطاء بشكل آمن

### 📝 التوثيق - Documentation
- إضافة تعليقات توضيحية باللغة العربية
- توثيق الوظائف باستخدام docstrings
- إنشاء ملف README.md شامل

## كيفية المساهمة - How to Contribute
1. قم بعمل fork للمشروع
2. أنشئ فرع جديد (`git checkout -b feature/AmazingFeature`)
3. قم بعمل commit للتغييرات (`git commit -m 'Add some AmazingFeature'`)
4. ارفع التغييرات (`git push origin feature/AmazingFeature`)
5. افتح طلب Pull Request

## ملاحظات للمطورين - Notes for Developers
- تأكد من تثبيت المكتبات المطلوبة: `pip install cryptography`
- استخدم البيئة الافتراضية: `.venv`
- اتبع معايير الترميز المعتمدة في المشروع 