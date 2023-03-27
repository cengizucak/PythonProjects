

Dekoratörler, bir işlevin veya sınıfın davranışını değiştirmesine izin verdiği için Python'da çok güçlü ve kullanışlı bir araçtır. Dekoratörler, sarılmış fonksiyonun davranışını kalıcı olarak değiştirmeden genişletmek için başka bir fonksiyonu sarmamıza izin verir. Temel olarak, bir dekoratör bir işlevi alır, bazı işlevler ekler ve onu döndürür

Pytest - Fixtures =>
Fikstürler, uygulandığı her test fonksiyonundan önce çalışacak fonksiyonlardır. Fikstürler, veritabanı bağlantıları, test edilecek URL'ler ve bir tür girdi verileri gibi bazı verileri testlere beslemek için kullanılır. Bu nedenle, her test için aynı kodu çalıştırmak yerine, testlere fikstür işlevi ekleyebiliriz ve her testi gerçekleştirmeden önce çalışır ve verileri teste döndürür.

Pytest - Parameterizing Tests =>
Acikca ifade etmek gerekirse, parametreleştirme, matematiksel bir denklemde bir veya daha fazla katsayıyı değiştirme (değiştirme) işlemidir. Test bağlamında parametreleştirme, aynı testi hazırlanmış bir setten farklı değerlerle çalıştırma işlemidir. Test ve verilerin her bir kombinasyonu, yeni bir test durumu olarak sayılır.

Fixtures ile Parameterizearasindaki fark =>
Fixtures – bir test girişini bir kez tanımlamanıza ve bunu birçok test işlevinde paylaşmanıza olanak tanır.
Parameterize - tek bir test işlevi için birden çok test senaryosunu kolayca tanımlamanıza ve çalıştırmanıza olanak tanır.

pytest.mark.xfail => 
Bunu belirli testlerin başarısız olmasını beklediğinizi belirtmek için kullanıyoruz.

pytest.mark.timeout =>
Burda zaman kisitlamasi vardir. Test belli bir sure icinde tamamlanmalidir

pytest.mark.skip => 
Bununla bazi testleri atliyoruz..

pytest.mark.dependency =>
Dependency kelimesini bagimlilik olarak ogrendik. Sonuc olarak bununla testler arasinda bagimlikilari belirtiriz.

