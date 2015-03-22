/*
	change <cmd> <xxx/_yyy.tex> <...> ... => <cmd> <xxx/yyy.tex> <...>
	set SumatraPDF to treas _yyy.tex as yyy.tex
	InverseSearchCmdLine = "c:\prog\ango\wrap_sumatra.exe" "/j%l" "%f"
*/
#include <stdio.h>
#include <cybozu/process.hpp>

//int main(int argc, char *argv[])
int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
	try
{
	int argc = __argc;
	char **argv = __argv;
	const std::string cmd = "c:/Program Files (x86)/Hidemaru/Hidemaru.exe";
	std::vector<std::string> param;
	for (int i = 1; i < argc; i++) {
		std::string p(argv[i]);
		const size_t len = p.size();
		if (len > 6 && p.compare(len - 4, 4, ".tex") == 0) {
			size_t pos = p.find_last_of("\\/");
			if (p[pos + 1] == '_') {
				p.erase(pos + 1, 1);
			}
		}
		param.push_back(p);
	}
	cybozu::Process proc;
	return proc.run(cmd, param) ? 0 : 1;
} catch (std::exception& e) {
	printf("ERR %s\n", e.what());
	return 1;
}
