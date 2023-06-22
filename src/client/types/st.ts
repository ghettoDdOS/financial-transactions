export interface STData {
  /**
   * Наименование получателя платежа
   */
  Name: string
  /**
   * Номер счета получателя платежа
   */
  PersonalAcc: string
  /**
   * Наименование банка получателя платежа
   */
  BankName: string
  /**
   * БИК
   */
  BIC: string
  /**
   * Номер кор./сч. банка получателя платежа
   */
  CorrespAcc: string
  Sum?: string
  Purpose?: string
  PayeeINN?: string
  PayerINN?: string
  DrawerStatus?: string
  KPP?: string
  CBC?: string
  OKTMO?: string
  PaytReason?: string
  TaxPeriod?: string
  Flat?: string
  DocNo?: string
  DocDate?: string
  TaxPaytKind?: string
  LastName?: string
  FirstName?: string
  MiddleName?: string
  PayerAddress?: string
  PersonalAccount?: string
  DocIdx?: string
  PensAcc?: string
  Contract?: string
  PersAcc?: string
  Phone?: string
  PayerIdType?: string
  PayerIdNum?: string
  ChildFio?: string
  BirthDate?: string
  PaymTerm?: string
  PaymPeriod?: string
  Category?: string
  ServiceName?: string
  CounterId?: string
  CounterVal?: string
  QuittId?: string
  QuittDate?: string
  InstNum?: string
  ClassNum?: string
  SpecFio?: string
  AddAmount?: string
  RuleId?: string
  ExecId?: string
  RegType?: string
  UIN?: string
  TechCode?: string
  date?: string
}

export enum STEncoding {
  WIN1251 = 1,
  UTF8 = 2,
  'KOI8-R' = 3
}

export interface STHeader {
  identifier: string
  version: number
  encoding: STEncoding
  delimiter: string
}
