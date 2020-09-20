graph [
  node [
    id 0
    label 1
    disk 6
    cpu 3
    memory 2
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 52
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 169
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 85
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 120
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 154
  ]
  edge [
    source 3
    target 5
    delay 30
    bw 198
  ]
]
