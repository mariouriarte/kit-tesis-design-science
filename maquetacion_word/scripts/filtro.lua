-- Filtro pandoc: rótulos APA de tablas/figuras y notas con estilos propios.
-- No altera texto: solo asigna estilos de párrafo y une rótulo+título cuando
-- el Markdown los separa en dos párrafos (tablas de anexos).

local function texto(inl)
  return pandoc.utils.stringify(inl)
end

local function etiqueta(first)
  if first == nil or first.t ~= "Strong" then return nil end
  local t = texto(first)
  return t:match("^(Tabla) [%w%.]+$") or t:match("^(Figura) [%w%.]+$")
end

local function rotulo_div(kind, content)
  local style = (kind == "Tabla") and "Rotulo Tabla" or "Rotulo Figura"
  return pandoc.Div({ pandoc.Para(content) }, pandoc.Attr("", {}, { ["custom-style"] = style }))
end

function Blocks(blocks)
  local out = {}
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    if b.t == "Para" and #b.content > 0 then
      local first = b.content[1]
      local kind = etiqueta(first)
      if kind then
        if #b.content == 1 and blocks[i + 1] and blocks[i + 1].t == "Para"
           and #blocks[i + 1].content >= 1 and blocks[i + 1].content[1].t == "Emph" then
          -- rótulo y título en párrafos separados: se unen con salto de línea
          local content = { first, pandoc.LineBreak() }
          for _, x in ipairs(blocks[i + 1].content) do table.insert(content, x) end
          table.insert(out, rotulo_div(kind, content))
          i = i + 2
        else
          table.insert(out, rotulo_div(kind, b.content))
          i = i + 1
        end
      elseif first.t == "Emph" and texto(first) == "Nota." then
        table.insert(out, pandoc.Div({ pandoc.Para(b.content) }, pandoc.Attr("", {}, { ["custom-style"] = "Nota" })))
        i = i + 1
      else
        table.insert(out, b)
        i = i + 1
      end
    else
      table.insert(out, b)
      i = i + 1
    end
  end
  return out
end
