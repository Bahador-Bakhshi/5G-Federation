graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 9
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 14
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 16
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 88
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 126
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 96
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 168
  ]
  edge [
    source 1
    target 5
    delay 33
    bw 192
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 50
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 98
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 103
  ]
]
