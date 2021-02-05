graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 4
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 9
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 8
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 2
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 14
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 158
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 192
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 200
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 100
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 77
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 200
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 150
  ]
]
