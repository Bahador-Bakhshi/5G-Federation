graph [
  node [
    id 0
    label 1
    disk 1
    cpu 3
    memory 13
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 7
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 16
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 74
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 186
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 147
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 60
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 140
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 105
  ]
]
