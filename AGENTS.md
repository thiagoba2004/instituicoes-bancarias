# AGENTS.md — Instituições Bancárias

**project_code:** `PRJ-000022`  
**project_name:** `Instituições Bancárias`  
**project_id_legacy:** `instituicoes-bancarias`  
**repository:** `thiagoba2004/instituicoes-bancarias`  
**generated_from_kernel:** `1.11`  
**generator_strategy:** `EA-000002-000025` (Gerador de Agents, Rota A)  
**classification:** `P2_GIT_PUBLICO_REPOSITORIO`

## 1. Estado da missão

Este Projeto possui **missão humana aprovada** em `REQ-000022-20261010-002`: estudar, organizar e comparar documentalmente bancos e instituições financeiras brasileiras. O público-alvo, primeiras entregas e respectivos critérios de aceite ainda exigem delimitação e prova próprias; não reabrir aprovação da missão. O titular aprovou a recomendação de Projeto ChatGPT especializado com C3, mas vínculo B1, configuração nativa C3 e recebimento A6 não estão tecnicamente comprovados. Não prestar serviços financeiros, coletar dados privados de clientes nem alegar representação institucional.

## 2. Fonte normativa e continuidade

Este AGENTS incorpora por referência os princípios universais vigentes do `thiagoba2004/gerador-de-agents/AGENTS_KERNEL.md` versão `1.11`, sem se sobrepor a regras locais futuras mais rigorosas. Para este Projeto: `AGENTS.md` → documentos locais específicos → `PROJECT_STATE.json` → `STRATEGY_LOG.jsonl` / `REQUEST_LOG.jsonl` → Git histórico → memória de conversa.

Todo pedido substantivo deve ser registrado em `REQUEST_LOG.jsonl`, tecnicamente verificado e vinculado a uma Estratégia Autônoma e Plano de Fases locais antes da execução. Não inventar decisões, fontes, capacidades, alterações Git, publicação ou testes.

## 3. Identidade canônica

- Projeto: `PRJ-000022`.
- Estratégia local: `EA-000022-EEEEEE`.
- Fase: `F-000022-EEEEEE-FFF`.

Códigos são monotônicos, únicos e independentes de nomes. Preservar logs append-only. Esta inicialização usa `EA-000022-000001`, com plano em `estrategias/EA-000022-000001-bootstrap-rota-a.md`.

## 4. Uso do Gerador e módulos

Perfil canônico no Gerador: `thiagoba2004/gerador-de-agents/profiles/instituicoes-bancarias.json`. Ativados inicialmente apenas `execution-environments` e `information-classification` por se tratar de Projeto persistente em Git público. Módulos de pesquisa, publicação, site, jurídico, software, dados, ensino ou automação requerem finalidade comprovada e ativação registrada.

Acesso público ao GitHub **não equivale** a site próprio ou GitHub Pages habilitado. Sem autorização específica, não configurar hospedagem, construir interface, abrir formulário ou prestar serviço.

## 5. Classificação, segurança e honestidade

O repositório é público. Proibido enviar credenciais, informações S2+, extratos bancários, informações de clientes, dados acadêmicos privados, casos sigilosos e documentos confidenciais. Somente dados públicos e arquivos internos não sensíveis expressamente revisados poderão ser publicados. Considerar a história Git pública; um branch não é cofre.

Distinguir `PLANEJADO`, `SALVO`, `VERSIONADO`, `PUBLICADO` e `VERIFICADO`. Não apresentar fontes de domínio como verificadas sem consulta e referência.

## 6. Próximos gates de handoff e SCIV

A EA-000022-000001 foi concluída tecnicamente. A missão aprovada está formalizada em `EA-000022-000002`, permanecendo pendentes instalação humana das Instruções nativas, prova de vínculo/contexto C3 e teste A6 especializado. O SCIV sob demanda pertence exclusivamente à EA-000022-000003, com alterações de código e testes reservados ao Codex no repositório local, e não será ativado antes de provisionamento/readback. A governança não deve gerar tarefas apenas para justificar sua existência.

## Adaptador ChatGPT — persistência independente da plataforma

**Origem da correção:** autorização humana de portabilidade `REQ-20261010-006` (Gerador de Agents), vinculada à Governança Geral `REQ-GLOBAL-20261010-017`.

O arquivo local [`adaptadores/chatgpt/INSTRUCOES.md`](adaptadores/chatgpt/INSTRUCOES.md) preserva, **dentro deste repositório GitHub**, a versão integral das Instruções destinadas ao campo **Instruções** do Projeto ChatGPT associado a `PRJ-000022`. Ele foi inicialmente gerado pelo `PRJ-000002 — Gerador de Agents`, sob `handoffs/chatgpt/PRJ-000022-INSTRUCOES.md`.

**Separação de responsabilidades:** este `AGENTS.md`, as políticas locais, os logs e o `PROJECT_STATE.json` continuam definindo regras e estado canônicos independentes do fornecedor. `adaptadores/chatgpt/INSTRUCOES.md` é um **adaptador específico da interface ChatGPT**, utilizável para reconstruir a configuração caso se troque de conversa, plataforma ou dispositivo; não substitui o kernel universal nem concede poderes extras à IA.

**Atualização e prova:** ao revisar o adaptador, versionar a mudança em GitHub, confrontar `AGENTS.md` e `PROJECT_STATE.json`, e depois atualizar/conferir **manualmente** as Instruções efetivas na interface ChatGPT. O conteúdo no Git **não se sincroniza automaticamente** com a interface. Sem confirmação da configuração real, não declarar o vínculo de memória C2/C3 efetivado nem o Gate de handoff **A6/B8** aceito. Se este adaptador divergir do estado do Projeto, identificar a divergência e reconciliar de forma autorizada, sem apagar histórico.

**Publicação e segurança:** este repositório é público. Não inserir informações S2+, credenciais ou dados privados no adaptador ou em qualquer arquivo versionado. As restrições de execução por `action_id`, autorização, proveniência e classificação permanecem vinculantes.

## Padrão canônico de recebimento operacional A6/B8

**Decisão de padronização transversal:** `REQ-GLOBAL-20261010-018` e `PRJ-000002:REQ-20261010-007`. O relatório integral do teste inicial do **Gate A6** encontra-se em [`governanca/recebimentos/2026-10-10-prj-000022-gate-a6.md`](governanca/recebimentos/2026-10-10-prj-000022-gate-a6.md); o índice de recebimentos e a convenção estão em [`governanca/recebimentos/README.md`](governanca/recebimentos/README.md). Caminhos anteriores são **ponteiros de compatibilidade**, não relatórios concorrentes.

Em todo teste futuro do recebimento, registrar o pedido, executar leitura comprovada dos arquivos locais, elaborar relatório com evidências, matriz de requisitos, pendências e próximo passo, e **salvar no mesmo repositório GitHub** sob `governanca/recebimentos/AAAA-MM-DD-prj-NNNNNN-gate-a6.md` (data real, `PRJ` local). Para dois testes no mesmo dia, usar `-r02`, `-r03`; nunca apagar ou sobrescrever a evidência histórica para simular avanço. Somente declarar salvamento depois de commit e leitura de retorno verificáveis.

O Chat especializado deve receber **Instruções e prompt de homologação com caminho e regra de persistência**, conforme a seção 7 de `thiagoba2004/gerador-de-agents/GERADOR_WORKFLOW.md`. Se o conector não puder escrever, fornecer o Markdown completo e registrar `NOT_PERSISTED`, sem simular GitHub. A cópia do adaptador `adaptadores/chatgpt/INSTRUCOES.md` permanece versionada; não presumir sincronização automática com a configuração da interface ChatGPT.

Este índice e a migração não demonstram vínculo administrativo do Projeto ChatGPT, C3 efetivo, publicação de Site/Pages ou aceitação integral do Gate A6. Preservar o estado verificado no `PROJECT_STATE.json` até cumprir os requisitos próprios de homologação. Conteúdo S2+, credenciais e dados não públicos **não devem entrar em Git público**.


## Estratégias atuais reconciliadas — 11/10/2026

- `EA-000022-000002` — missão aprovada/handoff C3, em andamento até prova nativa e A6; fonte `REQ-000022-20261010-002`.
- `EA-000022-000003` — SCIV ON_DEMAND, criada documentalmente e **aguardando CODEX** para caixas/adaptador/testes; fonte `REQ-000022-20261011-005` e `EA-000000-000034`. `enabled=false` até implantação provada.

Não confundir criação de Plano com execução técnica. Site Pages não autorizado; preservar a regra de classificação S0/S1 revisado em Git público.
