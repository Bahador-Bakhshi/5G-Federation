graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 13
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 1
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 192
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 100
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 141
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 93
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 50
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 109
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 99
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 92
  ]
]
