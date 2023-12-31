# Generated by Django 4.2.2 on 2023-06-15 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentReceipt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=160, verbose_name="Наименование получателя платежа"
                    ),
                ),
                (
                    "personal_acc",
                    models.CharField(
                        max_length=20, verbose_name="Номер счета получателя платежа"
                    ),
                ),
                (
                    "bank_name",
                    models.CharField(
                        max_length=45,
                        verbose_name="Наименование банка получателя платежа",
                    ),
                ),
                ("bic", models.CharField(max_length=9, verbose_name="БИК")),
                (
                    "corresp_acc",
                    models.CharField(
                        max_length=20,
                        verbose_name="Номер кор./сч. банка получателя платежа",
                    ),
                ),
                (
                    "sum",
                    models.CharField(
                        blank=True,
                        max_length=18,
                        null=True,
                        verbose_name="Сумма платежа, в копейках",
                    ),
                ),
                (
                    "purpose",
                    models.CharField(
                        blank=True,
                        max_length=210,
                        null=True,
                        verbose_name="Наименование платежа (назначение)",
                    ),
                ),
                (
                    "payee_inn",
                    models.CharField(
                        blank=True,
                        max_length=12,
                        null=True,
                        verbose_name="ИНН получателя платежа",
                    ),
                ),
                (
                    "payer_inn",
                    models.CharField(
                        blank=True,
                        max_length=12,
                        null=True,
                        verbose_name="ИНН плательщика",
                    ),
                ),
                (
                    "drawer_status",
                    models.CharField(
                        blank=True,
                        max_length=2,
                        null=True,
                        verbose_name="Статус составителя платежного документа",
                    ),
                ),
                (
                    "kpp",
                    models.CharField(
                        blank=True,
                        max_length=9,
                        null=True,
                        verbose_name="КПП получателя платежа",
                    ),
                ),
                (
                    "cbc",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="КБК"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Фамилия плательщика",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Имя плательщика",
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Отчество плательщика",
                    ),
                ),
                (
                    "payer_address",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Адрес плательщика",
                    ),
                ),
                (
                    "personal_account",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Лицевой счет бюджетного получателя",
                    ),
                ),
                (
                    "doc_idx",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Индекс платежного документа",
                    ),
                ),
                (
                    "pens_acc",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="№ лицевого счета в системе персонифицированного учета в ПФР - СНИЛС",
                    ),
                ),
                (
                    "contract",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер договора",
                    ),
                ),
                (
                    "pers_acc",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер лицевого счета плательщика в организации (в системе учета ПУ)",
                    ),
                ),
                (
                    "flat",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер квартиры",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "payer_id_type",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вид ДУЛ плательщика",
                    ),
                ),
                (
                    "payer_id_num",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер ДУЛ плательщика",
                    ),
                ),
                (
                    "child_fio",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Ф.И.О. ребенка/учащегося",
                    ),
                ),
                (
                    "birth_date",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "paym_term",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Срок платежа/дата выставления счета",
                    ),
                ),
                (
                    "paym_period",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Период оплаты",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вид платежа",
                    ),
                ),
                (
                    "service_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Код услуги/название прибора учета",
                    ),
                ),
                (
                    "counter_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер прибора учета",
                    ),
                ),
                (
                    "counter_val",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Показание прибора учета",
                    ),
                ),
                (
                    "quitt_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер извещения, начисления, счета",
                    ),
                ),
                (
                    "quitt_date",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Дата извещения/начисления/счета/постановления (для ГИБДД)",
                    ),
                ),
                (
                    "inst_num",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер учреждения (образовательного, медицинского)",
                    ),
                ),
                (
                    "class_num",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер группы детсада/класса школы",
                    ),
                ),
                (
                    "spec_fio",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="ФИО преподавателя, специалиста, оказывающего услугу",
                    ),
                ),
                (
                    "add_amount",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Сумма страховки/дополнительной услуги/Сумма пени (в копейках)",
                    ),
                ),
                (
                    "rule_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер постановления (для ГИБДД)",
                    ),
                ),
                (
                    "exec_id",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Номер исполнительного производства",
                    ),
                ),
                (
                    "reg_type",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Код вида платежа (например, для платежей в адрес Росреестра)",
                    ),
                ),
                (
                    "uin",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Уникальный идентификатор начисления",
                    ),
                ),
                (
                    "tech_code",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("01", "Мобильная связь, стационарный телефон"),
                            ("02", "Коммунальные услуги, ЖКХ"),
                            ("03", "ГИБДД, налоги, пошлины, бюджетные платежи"),
                            ("04", "Охранные услуги"),
                            ("05", "Услуги, оказываемые УФМС"),
                            ("06", "ПФР"),
                            ("07", "Погашение кредитов"),
                            ("08", "Образовательные учреждения"),
                            ("09", "Интернет и ТВ"),
                            ("10", "Электронные деньги"),
                            ("11", "Отдых и путешествия"),
                            ("12", "Инвестиции и страхование"),
                            ("13", "Спорт и здоровье"),
                            ("14", "Благотворительные и общественные организации"),
                            ("15", "Прочие услуги"),
                        ],
                        max_length=2,
                        null=True,
                        verbose_name="Технический код, рекомендуемый для заполнения поставщиком услуг. Может использоваться принимающей организацией для вызова соответствующей обрабатывающей ИТ-системы. Перечень значений кода представлен в Приложении Г.",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Квитанция об оплате",
                "verbose_name_plural": "Квитанции об оплате",
            },
        ),
    ]
