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


class PaymentReceipt(models.Model):
    user = models.ForeignKey(
        UserModel,
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        _("Наименование получателя платежа"),
        max_length=160,
    )
    personal_acc = models.CharField(
        _("Номер счета получателя платежа"),
        max_length=20,
    )
    bank_name = models.CharField(
        _("Наименование банка получателя платежа"),
        max_length=45,
    )
    bic = models.CharField(_("БИК"), max_length=9)
    corresp_acc = models.CharField(
        _("Номер кор./сч. банка получателя платежа"),
        max_length=20,
    )

    sum = models.CharField(
        _("Сумма платежа, в копейках"),
        max_length=18,
        blank=True,
        null=True,
    )
    purpose = models.CharField(
        _("Наименование платежа (назначение)"),
        max_length=210,
        blank=True,
        null=True,
    )
    payee_inn = models.CharField(
        _("ИНН получателя платежа"),
        max_length=12,
        blank=True,
        null=True,
    )
    payer_inn = models.CharField(
        _("ИНН плательщика"),
        max_length=12,
        blank=True,
        null=True,
    )
    drawer_status = models.CharField(
        _("Статус составителя платежного документа"),
        max_length=2,
        blank=True,
        null=True,
    )
    kpp = models.CharField(
        _("КПП получателя платежа"),
        max_length=9,
        blank=True,
        null=True,
    )
    cbc = models.CharField(
        _("КБК"),
        max_length=20,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        _("Фамилия плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    first_name = models.CharField(
        _("Имя плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    middle_name = models.CharField(
        _("Отчество плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    payer_address = models.CharField(
        _("Адрес плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    personal_account = models.CharField(
        _("Лицевой счет бюджетного получателя"),
        blank=True,
        null=True,
        max_length=255,
    )
    doc_idx = models.CharField(
        _("Индекс платежного документа"),
        blank=True,
        null=True,
        max_length=255,
    )
    pens_acc = models.CharField(
        _("№ лицевого счета в системе персонифицированного учета в ПФР - СНИЛС"),
        blank=True,
        null=True,
        max_length=255,
    )
    contract = models.CharField(
        _("Номер договора"),
        blank=True,
        null=True,
        max_length=255,
    )
    pers_acc = models.CharField(
        _("Номер лицевого счета плательщика в организации (в системе учета ПУ)"),
        blank=True,
        null=True,
        max_length=255,
    )
    flat = models.CharField(
        _("Номер квартиры"),
        blank=True,
        null=True,
        max_length=255,
    )
    phone = models.CharField(
        _("Номер телефона"),
        blank=True,
        null=True,
        max_length=255,
    )
    payer_id_type = models.CharField(
        _("Вид ДУЛ плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    payer_id_num = models.CharField(
        _("Номер ДУЛ плательщика"),
        blank=True,
        null=True,
        max_length=255,
    )
    child_fio = models.CharField(
        _("Ф.И.О. ребенка/учащегося"),
        blank=True,
        null=True,
        max_length=255,
    )
    birth_date = models.CharField(
        _("Дата рождения"),
        blank=True,
        null=True,
        max_length=255,
    )
    paym_term = models.CharField(
        _("Срок платежа/дата выставления счета"),
        blank=True,
        null=True,
        max_length=255,
    )
    paym_period = models.CharField(
        _("Период оплаты"),
        blank=True,
        null=True,
        max_length=255,
    )
    category = models.CharField(
        _("Вид платежа"),
        blank=True,
        null=True,
        max_length=255,
    )
    service_name = models.CharField(
        _("Код услуги/название прибора учета"),
        blank=True,
        null=True,
        max_length=255,
    )
    counter_id = models.CharField(
        _("Номер прибора учета"),
        blank=True,
        null=True,
        max_length=255,
    )
    counter_val = models.CharField(
        _("Показание прибора учета"),
        blank=True,
        null=True,
        max_length=255,
    )
    quitt_id = models.CharField(
        _("Номер извещения, начисления, счета"),
        blank=True,
        null=True,
        max_length=255,
    )
    quitt_date = models.CharField(
        _("Дата извещения/начисления/счета/постановления (для ГИБДД)"),
        blank=True,
        null=True,
        max_length=255,
    )
    inst_num = models.CharField(
        _("Номер учреждения (образовательного, медицинского)"),
        blank=True,
        null=True,
        max_length=255,
    )
    class_num = models.CharField(
        _("Номер группы детсада/класса школы"),
        blank=True,
        null=True,
        max_length=255,
    )
    spec_fio = models.CharField(
        _("ФИО преподавателя, специалиста, оказывающего услугу"),
        blank=True,
        null=True,
        max_length=255,
    )
    add_amount = models.CharField(
        _("Сумма страховки/дополнительной услуги/Сумма пени (в копейках)"),
        blank=True,
        null=True,
        max_length=255,
    )
    rule_id = models.CharField(
        _("Номер постановления (для ГИБДД)"),
        blank=True,
        null=True,
        max_length=255,
    )
    exec_id = models.CharField(
        _("Номер исполнительного производства"),
        blank=True,
        null=True,
        max_length=255,
    )
    reg_type = models.CharField(
        _("Код вида платежа (например, для платежей в адрес Росреестра)"),
        blank=True,
        null=True,
        max_length=255,
    )
    uin = models.CharField(
        _("Уникальный идентификатор начисления"),
        blank=True,
        null=True,
        max_length=255,
    )
    tech_code = models.CharField(
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

    class Meta:
        verbose_name = _("Квитанция об оплате")
        verbose_name_plural = _("Квитанции об оплате")

    def __str__(self) -> str:
        return (
            f"{self.name}-{self.personal_acc}-"
            f"{self.bank_name}-{self.bic}-{self.corresp_acc}"
        )
