graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 11
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 1
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 111
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 89
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 185
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 102
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 163
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 151
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 193
  ]
]
