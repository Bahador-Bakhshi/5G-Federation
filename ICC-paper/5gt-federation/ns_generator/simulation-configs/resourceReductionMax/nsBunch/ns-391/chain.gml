graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 4
    memory 14
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 1
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 189
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 129
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 54
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 55
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 58
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 144
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 150
  ]
]
