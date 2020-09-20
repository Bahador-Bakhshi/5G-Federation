graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 12
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 4
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 9
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 160
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 118
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 131
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 147
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 175
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 121
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 106
  ]
]
