
' convert pptx to pdf

Option Explicit
Dim g_fs
set g_fs = wscript.createObject("scripting.fileSystemObject")

ParseAndRun wscript.arguments
wscript.quit

sub ParseAndRun(args)
	Dim inName, outName
	if args.unnamed.Count = 0 then
		wscript.echo "pptx2pdf.vbs inName [outFileName]"
		wscript.quit
	end if

	inName = g_fs.getAbsolutePathName(args.unnamed(0))
	Dim suf
	suf = lcase(g_fs.getExtensionName(inName))
	if suf <> "ppt" and suf <> "pptx" then
		wscript.echo "bad suffix=" & suf
		wscript.quit
	end if

	if args.unnamed.Count < 2 then
		outName = g_fs.getParentFolderName(inName) + "\" + g_fs.getBaseName(inName) + ".pdf"
	else
		outName = g_fs.getAbsolutePathName(args.unnamed(1))
	end if

	pptx2pdf inName, outName
end sub

sub pptx2pdf(inName, outName)
	on error resume next

	Dim app, presen
	set app = createObject("powerPoint.application")

	set presen = app.presentations.open(inName) ', ReadOnly = true
	presen.saveAs outName, 32, true
	app.quit
	if err.number <> 0 then
		wscript.echo "ERR:" & err.number & " desc:" & err.description
	end if
end sub
