# Evidências offline — EA-000022-000003 F002–F004

Classificação S0_PUBLICO / P2_GIT_PUBLICO_REPOSITORIO. Fixtures são sintéticas; nenhum recibo real ou autorização operacional foi produzido.

Executar `python -B governanca/testes-sciv/run_checks.py` com Python 3.12+, `jsonschema` e suas dependências instaladas. Nesta sessão foi usado o Python do runtime Codex e `PYTHONPATH` apontando para dependências já existentes em `../.venvs/sciv-issue5/Lib/site-packages`; `PYTHONUTF8=1` corrige a codificação de subprocessos no Windows. Sem instalação ou gasto. `provision.py` é o provisionamento inicial, e recusa adaptador com bloco existente. O runner recompõe somente o bloco a partir do baseline cujo hash foi registrado; não concede vínculo nem modifica o perfil externo do Gerador.

`composition.json` registra hashes dos bytes do checkout (CRLF fora do bloco); Git normaliza LF conforme `core.autocrlf=true`. O teste compara os bytes originais fora do bloco e a composição idempotente. Readback Git compara blobs canônicos separadamente.

Resultados: 8 testes locais finais passaram; 61 testes Gerador passaram; suíte runtime externa: 156 executados, 153 passaram, uma falha e dois erros. Retry UTF-8: recuperação CLI passou; symlink continuou WinError 1314 mesmo com execução fora do sandbox. Portanto 154/156 cenários externos passaram após retry; sem ocultar a execução inicial em `runtime.log`.

Falha externa `test_changed_branch_blocks`: fixture define branch `main`, agora igual à rota `main`, portanto não há mismatch. O teste local suplementar usa branch realmente diferente e passa. Código externo não foi alterado. Teste symlink continua bloqueado pelo privilégio Windows, sem mudança de permissões.

Gate Gerador Rota A `sciv`: FAIL por `FIRST_EA_ACTION_PLAN_UNVERIFIED`, matriz ausente da EA histórica 000001. O gate foi executado sem exceção, rota alternativa ou fixture de aprovação. Correção histórica compete à governança; nenhuma aprovação antiga deve ser inventada. F004 não é VERIFIED.

O ambiente virtual existente não inicia porque seu Python original está ausente. A primeira execução com Python Codex identificou dependência jsonschema ausente e divergência de hash decorrente de normalização LF/CRLF no runner. Essas condições de execução foram corrigidas com dependências existentes e reconstrução do baseline verificada por hash; testes locais finais passaram.

Sem workflow CI local preexistente; CI não introduzida. Tests upstream usam diretórios temporários, sem bytecode (`-B`); nenhum código do Gerador ou G0 modificado.
