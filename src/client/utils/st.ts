import type { STData, STHeader } from '@/types/st'

const ST_DATA_REQUIRED_FIELDS = ['Name', 'PersonalAcc', 'BankName', 'BIC', 'CorrespAcc']
const STANDARD_IDENTIFIER = 'ST'

const STHeaderRegExp = new RegExp(`^${STANDARD_IDENTIFIER}(\\d{4})(\\d){1}(\\D)`)

class STParseError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'STParseError'
  }
}

export const ST = {
  /**
   * Парсит строку с платежными данными зашифрованными в стандарте ST
   * @param text ST строка
   * @returns Данные для оплаты
   * @throws STParseError При неверном формате входных данных вызывается исключение
   */
  parse(text: string): STData {
    const headerData = text.match(STHeaderRegExp)
    if (headerData === null) throw new STParseError('Неверный стандарт данных')

    const header: STHeader = {
      identifier: STANDARD_IDENTIFIER,
      version: parseInt(headerData[1]),
      encoding: parseInt(headerData[2]),
      delimiter: headerData[3]
    }
    const data = Object.fromEntries(
      text
        .slice(8)
        .split(header.delimiter)
        .map((pair) => pair.split('='))
    )
    const parsedFields = Object.keys(data)

    ST_DATA_REQUIRED_FIELDS.forEach((key) => {
      if (!parsedFields.includes(key))
        throw new STParseError(`Отсутствует обязательное поле ${key}`)
    })

    return data
  }
}
