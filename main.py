import pypandoc
import subprocess

extension = 'beamer'
outputfilename = 'test.pdf'
pypandoc.convert_file('test.md',
                      to=extension,
                      outputfile=outputfilename,
                      format='markdown+yaml_metadata_block',
                      extra_args=['--reference-doc', 'template.pptx',
                                  # '--pdf-engine', 'xelatex',
                                  '--include-in-header', './mystyle.tex',
                                  # '--metadata-file', 'yaml.md',
                                  ],
                      )

subprocess.call(f"open '{outputfilename}'", shell=True)
