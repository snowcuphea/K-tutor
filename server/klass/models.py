from django.db import models


class Kw(models.Model):
    content_kor = models.CharField(max_length=30)
    count = models.IntegerField()


class Cs(models.Model):
    name_kor = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100, default="Need to add")
    type = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    imgurl = models.TextField(default="Need to add")


class Cpct(models.Model):
    kor = models.TextField()
    eng = models.TextField()
    main_kw = models.ForeignKey(Kw, on_delete=models.CASCADE)
    cs = models.ForeignKey(Cs, on_delete=models.CASCADE)


class Cpcq(models.Model):
    kor = models.TextField()
    eng = models.TextField()
    kcq = models.ManyToManyField(Kw, related_name="contained_cpcq")


class Lc(models.Model):
    cs = models.ForeignKey(Cs, on_delete=models.CASCADE)
    main_kw_index = models.IntegerField()
    main_kw_kor = models.TextField()
    main_kw_eng = models.TextField()
    main_kw = models.ForeignKey(Kw, on_delete=models.CASCADE)
    meaning = models.TextField()
    before_kor = models.TextField()
    before_eng = models.TextField()
    cpct_kor = models.TextField()
    cpct_eng = models.TextField()
    after_kor = models.TextField()
    after_eng = models.TextField()
    example_kor = models.TextField()
    example_eng = models.TextField(default="Need to add")
    imgurl = models.TextField(default="Need to add")
