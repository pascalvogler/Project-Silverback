import spell_list
import spell_modifier_list
import element_list

class Spell:
  def __init__(self, name, damage, mana_cost, element=None,  effect=None, crit=0):
    self.name = name
    self.mana_cost = mana_cost
    self.element = element
    self.damage = damage
    self.effect = effect
    self.crit = crit

  def __str__(self):
    return self.name+' does '+str(self.damage)+' damage and has crit chance of '+str(int(self.crit*100))+' %'

  @property
  def string_display(self):
    _string = self.name + " Damage: " + str(self.damage) + " Mana Cost: " + str(self.mana_cost)
    return _string


def summonSpell(spell, element=None, modifier=None):
  '''Takes following arguments:
  spell: has to be in spell_list.py
  element: has to be in element_list.py
  modifier: has to be in spell_modifier_list.py

  Returns an object of Spell class'''

  # Copy base spell from spell_list
  summoned_spell = getattr(spell_list,spell).copy()

  # Add element to spell if given
  if(element!=None):

    # Get list of possible elements
    el = getattr(element_list,element)
    summoned_spell['element'] = el['element']

    #Add 'of element name' after spell name
    summoned_spell['name'] = summoned_spell['name']+" of "+el['name']

  # Add modifiers to spell if given
  if(modifier!=None):
    mod = getattr(spell_modifier_list,modifier)
    for item in mod['modifiers']:
      if item in summoned_spell:
        summoned_spell[item]*=mod['modifiers'][item]
    # Reset damage and mana_cost to ints, because applying modifiers leads to floating point errors
    summoned_spell['mana_cost']= int(summoned_spell['mana_cost'])
    summoned_spell['damage']= int(summoned_spell['damage'])

    # Add modifier in front of spell name 
    summoned_spell['name'] = mod['name'] +" "+ summoned_spell['name']
  return Spell(**summoned_spell)