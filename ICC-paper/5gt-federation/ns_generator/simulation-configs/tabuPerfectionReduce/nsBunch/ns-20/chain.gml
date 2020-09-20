graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 16
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 155
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 131
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 89
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 65
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 189
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 84
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 172
  ]
]
