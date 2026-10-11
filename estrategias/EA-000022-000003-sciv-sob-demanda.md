# EA-000022-000003 — Implantação SCIV Essencial Sob Demanda

**PRJ:** PRJ-000022 — Instituições Bancárias. **Autoridade:** REQ-GLOBAL-20261011-001 / EA-000000-000034 F003; opt-in autorizado. **Estado inicial:** PLANNED_AWAITING_CODEX; sem provisionamento. **Relação:** EA-000022-000002 trata da missão/handoff C3, não do SCIV.

## Finalidade
Implantar as duas caixas documentais SCIV no próprio `thiagoba2004/instituicoes-bancarias` em `main`, versão integral de Instruções com bloco gerenciado, `SCIV_STATE.mode=ON_DEMAND`, leitura somente quando solicitada pelo titular, testes negativos/positivos, tratamento e arquivo bilateral real. Sem cron, polling, webhooks, ativação automática, PEP live presumido ou dados S2+ no Git público.

## Plano de Fases
1. **F-000022-000003-001 — Admissão local:** reconciliar PRJ, sequência, mandato, WIP, EA-000022-000002, perfil, plano e registro dual; gate `SCIV_ADMISSAO_REGISTRADA`.
2. **F-000022-000003-002 — Caixas e estado:** CODEX provisiona inbox/outbox, históricos, `SCIV_STATE.json`, classificação e readback; gate `CAIXAS_VERSIONADAS`.
3. **F-000022-000003-003 — Instruções versionadas:** CODEX atualiza só bloco gerenciado no adaptador integral sem destruir missão/C3; gate `INSTRUCOES_VERSIONADAS`.
4. **F-000022-000003-004 — Regressões:** CODEX executa testes offline de idempotência, política, ativação expressa e `--gate sciv`; gate `SCIV_REPO_VERIFICADO`.
5. **F-000022-000003-005 — Instalação e recebimento A6:** titular instala Instruções atuais, G0 publica novo Comunicado a partir do A6 histórico, IA especializada responde com novo relatório; gate `A6_POS_INSTALACAO_CLASSIFICADO`.
6. **F-000022-000003-006 — Comportamento real e arquivo:** confirmar ausência de leitura automática, leitura sob pedido, resposta correlacionada, recibo e arquivamento após tratamento; gate `SCIV_COMPORTAMENTO_CLASSIFICADO`.

## Executor e fronteiras
As fases 002–004 dependem **exclusivamente de Codex CLI local no checkout PRJ-000022**, sujeito a autorização/gates; CHAT/G0 apenas coordena e registra documentos de governança. F005 requer ato humano na interface do ChatGPT, e a IA especializada só lê mensagens após pedido do titular. Site Pages não autorizado; não modificar bibliotecas, dados bancários privados ou estratégia de missão. A criação desta EA **não** prova nenhuma implantação.

**Matriz:** [EA-000022-000003-actions.json](EA-000022-000003-actions.json). Status de cada ação permanece PLANNED até evidência real. Registros globais são derivados dos arquivos locais com readback.
