string = 'HVqxBjoZ!?GkqdeOEezAE!?ohNjqRuxojy!?esAX!?dLsZc!? VcpGtt!?gOxjFQkzTDy!?etEyySXt!?dMVfSG!?akOgOdFpje!?aZpjG!?nydTfnQ!q!? nmanp!?aCa!?lIYeTdIl!?l!yYZyVI!?eOm!?mfcBM!?aNteYpX!?aGFlGtW!?lSy!XYh!?,TfgEb!? uD K!?oqpjKodZrz!?mEm r!?ddo!?aFUpe!qwj!?tvZo!? qKBspNfS!?iQXfEoo!?kGSdJlWh!? VTKzOZq!?jdSLdJdKAv!?aVTKun!?rQEvJ!?ictXgAKZY!?gbIdxqGSp!? aEfGvYgv!?bWgDdYZ!?eB !?ngAt!!? D qLljmm!?vhtTdpIqoJZ!?oQyJXBHX!?lupz!?gYAVXXNg!?taWDDVBQDSO!? BQO HIOZLY!?eoTXtn!?eyR!?nYZkIf!?  OrFk!?kJenGc!?lElWj!?e hOwVlpWz!?iVF!?nu odOVXvSP!?ebinLp!? fRwfXGQs!?tWdfhPh!?ruTvo!!?aHBj!PZaHtQ!?kYYk!?tWeNjDqV!?aFMctpAli!?tnIz!?ivq!?eGRNQq!?!KbotZVm'
l1 = ''
l2 = ''
target = ''
for letter in string:
    if l1 == '!' and l2 == '?':
        target += letter
    l1 = l2
    l2 = letter

print(target)