graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 13
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 147
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 186
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 198
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 159
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 158
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 122
  ]
]
