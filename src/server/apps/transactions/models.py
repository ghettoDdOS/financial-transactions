from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class TechCode(models.TextChoices):
    PHONE = "01", _("Мобильная связь, стационарный телефон")
    COMMUNAL_SERVICES = "02", _("Коммунальные услуги, ЖКХ")
    GIBDD = "03", _("ГИБДД, налоги, пошлины, бюджетные платежи")
    SECURITY = "04", _("Охранные услуги")
    FMS = "05", _("Услуги, оказываемые УФМС")
    FIU = "06", _("ПФР")
    CREDIT = "07", _("Погашение кредитов")
    EDUCATION = "08", _("Образовательные учреждения")
    INTERNET = "09", _("Интернет и ТВ")
    MONEY = "10", _("Электронные деньги")
    REST = "11", _("Отдых и путешествия")
    INVESTMENT = "12", _("Инвестиции и страхование")
    SPORT = "13", _("Спорт и здоровье")
    CHARITY = "14", _("Благотворительные и общественные организации")
    OTHER = "15", _("Прочие услуги")


class PaymentCategory(models.Model):
    name = models.CharField(verbose_name=_("Наименование категории"), max_length=150)

    class Meta:
        verbose_name = _("Категория платежа")
        verbose_name_plural = _("Категории платежей")

    def __str__(self) -> str:
        return self.name


class PaymentReceipt(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to=PaymentCategory,
        verbose_name=_("Категория"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    Name = models.CharField(
        _("Наименование получателя платежа"),
        max_length=160,
    )
    PersonalAcc = models.CharField(
        _("Номер счета получателя платежа"),
        max_length=20,
    )
    BankName = models.CharField(
        _("Наименование банка получателя платежа"),
        max_length=45,
    )
    BIC = models.CharField(_("БИК"), max_length=9)
    CorrespAcc = models.CharField(
        _("Номер кор./сч. банка получателя платежа"),
        max_length=20,
    )

    Sum = models.CharField(
        _("Сумма платежа, в копейках"),
        max_length=18,
        blank=True,
        null=True,
    )
    Purpose = models.CharField(
        _("Наименование платежа (назначение)"),
        max_length=210,
        blank=True,
        null=True,
    )
    PayeeINN = models.CharField(
        _("ИНН получателя платежа"),
        max_length=12,
        blank=True,
        null=True,
    )
    PayerINN = models.CharField(
        _("ИНН плательщика"),
        max_length=12,
        blank=True,
        null=True,
    )
    DrawerStatus = models.CharField(
        _("Статус составителя платежного документа"),
        max_length=2,
        blank=True,
        null=True,
    )
    KPP = models.CharField(
        _("КПП получателя платежа"),
        max_length=9,
        blank=True,
        null=True,
    )
    CBC = models.CharField(
        _("КБК"),
        max_length=20,
        blank=True,
        null=True,
    )

    LastName = models.CharField(
        _("Фамилия плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    FirstName = models.CharField(
        _("Имя плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    MiddleName = models.CharField(
        _("Отчество плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    PayerAddress = models.CharField(
        _("Адрес плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    PersonalAccount = models.CharField(
        _("Лицевой счет бюджетного получателя"),
        blank=True,
        null=True,
        max_length=255,
    )
    DocIdx = models.CharField(
        _("Индекс платежного документа"),
        blank=True,
        null=True,
        max_length=255,
    )
    PensAcc = models.CharField(
        _("№ лицевого счета в системе персонифицированного учета в ПФР - СНИЛС"),
        blank=True,
        null=True,
        max_length=255,
    )
    Contract = models.CharField(
        _("Номер договора"),
        blank=True,
        null=True,
        max_length=255,
    )
    PersAcc = models.CharField(
        _("Номер лицевого счета плательщика в организации (в системе учета ПУ)"),
        blank=True,
        null=True,
        max_length=255,
    )
    Flat = models.CharField(
        _("Номер квартиры"),
        blank=True,
        null=True,
        max_length=255,
    )
    Phone = models.CharField(
        _("Номер телефона"),
        blank=True,
        null=True,
        max_length=255,
    )
    PayerIdType = models.CharField(
        _("Вид ДУЛ плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    PayerIdNum = models.CharField(
        _("Номер ДУЛ плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    ChildFio = models.CharField(
        _("Ф.И.О. ребенка/учащегося"),
        blank=True,
        null=True,
        max_length=255,
    )
    BirthDate = models.CharField(
        _("Дата рождения"),
        blank=True,
        null=True,
        max_length=255,
    )
    PaymTerm = models.CharField(
        _("Срок платежа/дата выставления счета"),
        blank=True,
        null=True,
        max_length=255,
    )
    PaymPeriod = models.CharField(
        _("Период оплаты"),
        blank=True,
        null=True,
        max_length=255,
    )
    Category = models.CharField(
        _("Вид платежа"),
        blank=True,
        null=True,
        max_length=255,
    )
    ServiceName = models.CharField(
        _("Код услуги/название прибора учета"),
        blank=True,
        null=True,
        max_length=255,
    )
    CounterId = models.CharField(
        _("Номер прибора учета"),
        blank=True,
        null=True,
        max_length=255,
    )
    CounterVal = models.CharField(
        _("Показание прибора учета"),
        blank=True,
        null=True,
        max_length=255,
    )
    QuittId = models.CharField(
        _("Номер извещения, начисления, счета"),
        blank=True,
        null=True,
        max_length=255,
    )
    QuittDate = models.CharField(
        _("Дата извещения/начисления/счета/постановления (для ГИБДД)"),
        blank=True,
        null=True,
        max_length=255,
    )
    InstNum = models.CharField(
        _("Номер учреждения (образовательного, медицинского)"),
        blank=True,
        null=True,
        max_length=255,
    )
    ClassNum = models.CharField(
        _("Номер группы детсада/класса школы"),
        blank=True,
        null=True,
        max_length=255,
    )
    SpecFio = models.CharField(
        _("ФИО преподавателя, специалиста, оказывающего услугу"),
        blank=True,
        null=True,
        max_length=255,
    )
    AddAmount = models.CharField(
        _("Сумма страховки/дополнительной услуги/Сумма пени (в копейках)"),
        blank=True,
        null=True,
        max_length=255,
    )
    RuleId = models.CharField(
        _("Номер постановления (для ГИБДД)"),
        blank=True,
        null=True,
        max_length=255,
    )
    ExecId = models.CharField(
        _("Номер исполнительного производства"),
        blank=True,
        null=True,
        max_length=255,
    )
    RegType = models.CharField(
        _("Код вида платежа (например, для платежей в адрес Росреестра)"),
        blank=True,
        null=True,
        max_length=255,
    )
    UIN = models.CharField(
        _("Уникальный идентификатор начисления"),
        blank=True,
        null=True,
        max_length=255,
    )
    TechCode = models.CharField(
        _("Технический код, рекомендуемый для заполнения поставщиком услуг."),
        choices=TechCode.choices,
        help_text=_(
            "Может использоваться принимающей организацией для "
            "вызова соответствующей обрабатывающей ИТ-системы."
        ),
        blank=True,
        null=True,
        max_length=2,
    )

    date = models.DateTimeField(
        _("Дата"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Квитанция об оплате")
        verbose_name_plural = _("Квитанции об оплате")

    def __str__(self) -> str:
        return (
            f"{self.Name}-{self.PersonalAcc}-"
            f"{self.BankName}-{self.BIC}-{self.CorrespAcc}"
        )
