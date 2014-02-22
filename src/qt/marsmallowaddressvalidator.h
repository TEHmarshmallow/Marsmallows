#ifndef MarsmelloADDRESSVALIDATOR_H
#define MarsmelloADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator.
   Corrects near-miss characters and refuses characters that are not part of base58.
 */
class MarsmelloAddressValidator : public QValidator
{
    Q_OBJECT

public:
    explicit MarsmelloAddressValidator(QObject *parent = 0);

    State validate(QString &input, int &pos) const;

    static const int MaxAddressLength = 35;
};

#endif // MarsmelloADDRESSVALIDATOR_H
