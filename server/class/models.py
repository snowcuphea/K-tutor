from django.db import models


class Kw(models.Model):
    content = models.CharField(max_length=30)
    count = models.IntegerField()


class Cs(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    level = models.CharField(max_length=10)


class Cpct(models.Model):
    kor = models.TextField()
    eng = models.TextField()
    main_kw = models.ForeignKey(Kw, on_delete=models.PROTECT)
    cs = models.ForeignKey(Cs, on_delete=models.PROTECT)


class Cpcq(models.Model):
    kor = models.TextField()
    eng = models.TextField()
    kcq = models.ManyToManyField(Kw, related_name="contained_cpcq")


class Lc(models.Model):
    cs = models.ForeignKey(Cs, on_delete=models.CASCADE)
    main_kw_index = models.IntegerField(null=True)
    main_kw_word = models.TextField(null=True)
    main_kw = models.ForeignKey(Kw, on_delete=models.CASCADE)
    meaning = models.TextField(null=True)
    before_kor = models.TextField()
    before_eng = models.TextField()
    cpct_kor = models.TextField()
    cpct_eng = models.TextField()
    after_kor = models.TextField()
    after_eng = models.TextField()
    example = models.TextField()
