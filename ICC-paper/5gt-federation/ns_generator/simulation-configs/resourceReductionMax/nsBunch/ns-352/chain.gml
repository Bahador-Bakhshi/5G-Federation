graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 9
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 11
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 147
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 124
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 55
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 50
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 82
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 140
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 103
  ]
]
