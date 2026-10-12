# ROADMAP — Instituições Bancárias

**Projeto:** `PRJ-000022` · **Repositório:** `thiagoba2004/instituicoes-bancarias`  
**Estado:** `TECHNICAL_BOOTSTRAP_VERIFIED_SUBSTANTIVE_SCOPE_PENDING`  
**Gerador:** Rota A, `EA-000002-000025`.

## Estratégia vigente

**EA-000022-000001 — Inicialização técnica do Projeto pela Rota A.**

1. Fase 01/04: identidade, código e repositório público — concluída.
2. Fase 02/04: arquivos canônicos de persistência — em implantação.
3. Fase 03/04: perfil do Gerador e módulos fundamentados — pendente de verificação.
4. Fase 04/04: auditoria remota e fechamento técnico — pendente.

Plano: `estrategias/EA-000022-000001-bootstrap-rota-a.md`.

## Fronteira da inicialização

Apenas um **Projeto governável**, sem confundir isso com produto concluído, base de dados, curso oferecido ou site. Não realizar pesquisa nem criar serviços externos por inferência.

## Próximo passo substantivo

**`SUBSTANTIVE_SCOPE_AWAITING_HUMAN_DECISION`:** confirmar missão/finalidade, público-alvo, tipos de entregas e se deverá existir site próprio. Após essa definição, selecionar módulos e planejar trabalho local. Nenhuma atividade substantiva foi iniciada ou homologada.

## Verificação e encerramento técnico — 10/10/2026

A estratégia `EA-000022-000001` concluiu as quatro fases **exclusivamente de bootstrap técnico**, após readback no GitHub: identidade, oito fontes/arquivos mínimos, perfil Gerador, JSON/JSONL, classificação e visibilidade pública conferidos.

**Estado atual:** `TECHNICAL_BOOTSTRAP_VERIFIED_SUBSTANTIVE_SCOPE_PENDING`. O Projeto **não** tem missão detalhada aprovada, produto substantivo, pesquisa concluída, site Pages ou serviço implantado. O próximo gate é a decisão humana sobre finalidade, público-alvo, primeiros produtos e eventual site.


## Atualização canônica de 11/10/2026 — missão aprovada e SCIV separado

As seções anteriores descrevem o corte histórico do bootstrap de 10/10. A **missão substantiva foi aprovada** em `REQ-000022-20261010-002`: estudar, organizar e comparar documentalmente bancos e instituições financeiras brasileiras. Não solicitar nova aprovação dessa missão; delimitação de público e primeiras entregas permanece para fluxo especializado.

- **EA-000022-000002 — Missão aprovada e handoff especializado:** `estrategias/EA-000022-000002-missao-handoff-especializado.md`; `CREATED`, `IN_PROGRESS_HANDOFF_PENDING`, fase F003 (preparação/instalação C3). Titular aprovou C3 como recomendação; vínculo real e instalação permanecem NOT_VERIFIED; A6 pendente.
- **EA-000022-000003 — SCIV Essencial Sob Demanda:** `estrategias/EA-000022-000003-sciv-sob-demanda.md`; `CREATED`, `PLANNED_AWAITING_CODEX`, fase F001 documental preparada. **Sem caixas provisionadas, `enabled=false` e sem leitura automática.** Próxima implementação F002-F004, executor Codex CLI local no checkout do PRJ-000022, jamais G0/CHAT. Separação do domínio preservada.

**Gate local e global:** registrar dual no portfólio da Governança Geral com readback. Sem site Pages, serviços financeiros ou publicação sensível. A prova de registro não conclui gate `PRJ000022_SCIV_REPO_VERIFIED` da global `EA-000000-000034`.

## Execução CODEX F002–F004 — 11/10/2026

F002 e F003 verificadas documentalmente no commit `6700203cffa3ad1471aa68e78e40dea060a45790`, publicado e relido (19 blobs). Caixas locais vazias, adaptador integral com bloco SCIV e testes versionados. F004 BLOCKED: gate Rota A exige matriz histórica EA000001 ausente; fixture upstream de branch desatualizada e symlink Windows bloqueado. Oito testes locais e 61 Gerador passaram; runtime 154/156 cenários após retry UTF-8, sem aprovação integral. Relatório `auditorias/EA-000022-000003-codex-f002-f004-2026-10-11.md`.

Próximo passo: governança e owners resolvem bloqueios com mandato próprio, Codex repete gates falhos; F005 aguarda. `enabled=false`, instalação nativa, C3/A6 e comportamento real não comprovados. EA000002 preservada; EA SCIV e gate global não concluídos.


## Checkpoint G0 — 11/10/2026: remediação F004 sem backfill fictício

O resultado do Codex foi relido no GitHub: **EA-000022-000003 F002/F003 VERIFICADAS no repositório, F004 BLOCKED**. Correção independente documental em `adaptadores/chatgpt/INSTRUCOES.md` (commit `5d140d0`) reconciliou missão aprovada já persistida, escolha humana C3 **ainda não instalada nativamente**, mantendo o bloco SCIV. **EA-000022-000002 F003**: pacote pronto só em escopo de documentos; F004 A6 ainda pendente.

A G0 não criou matriz retroativa fictícia para a primeira EA de 10/10. A remediação de código será executada em `thiagoba2004/gerador-de-agents` pelo Codex (EA-000002-000027 ACT010) para compatibilidade com Rota A histórica; e na G0 pelo Codex (EA-000000-000034 ACT028) para fixture branch/symlink. Depois o Codex neste Projeto repetirá `EA-000022-000003 F004` com evidências reais. `enabled=false`, C3 nativo, A6 e comportamento real permanecem não comprovados. F003 global ainda não foi aceita. Referência G0: `auditorias/EA-000000-000034-F003-codex-prj000022-remediacoes-2026-10-11.md`.

## Reteste CODEX F004 ? 11/10/2026

F004/ACT-000022-000003-004: **VERIFIED_WITH_ENV_LIMITATION**, sem aceite integral. 8 locais PASS; 88 Gerador PASS; runtime 158 PASS + 1 SKIP f?sico WinError 1314; 12 PEP offline PASS. Gate sciv PASS, EA hist?rica NOT_BACKFILLED e matriz corrente PASS; bootstrap estrito FAIL esperado. Guard controlado e sensibilidade comprovados. Relat?rio: `auditorias/EA-000022-000003-codex-f004-retest-2026-10-11.md`. Depend?ncias imut?veis bd754a1/85a91ce verificadas; checkouts irm?os preservados. G0/governan?a local avalia o aceite da limita??o ou determina prova f?sica em ambiente compat?vel. F005 n?o iniciada; enabled=false; C3/A6/PEP live pendentes. Os registros anteriores permanecem cortes hist?ricos.
